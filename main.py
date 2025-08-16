import csv
import asyncio
from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
)
status = {"connected": False, "launched": False}
CSV_PATH = "abhyuday_flight.csv"

@app.get("/api/status")
async def get_status():
    return status

@app.post("/api/connect")
async def connect():
    status["connected"] = True
    status["launched"] = False
    return {"msg": "Flight controller connected."}

@app.post("/api/disconnect")
async def disconnect():
    status["connected"] = False
    status["launched"] = False
    return {"msg": "Flight controller disconnected."}

@app.post("/api/launch")
async def launch():
    if not status["connected"]:
        return {"msg": "Cannot launch: not connected."}
    status["launched"] = True
    return {"msg": "Launch initiated."}

@app.post("/api/reset")
async def reset():
    status["connected"] = False
    status["launched"] = False
    return {"msg": "All states reset."}

@app.websocket("/ws/telemetry")
async def telemetry_ws(ws: WebSocket):
    await ws.accept()
    flight_completed = False
    
    while True:
        if not (status["connected"] and status["launched"]):
            flight_completed = False
            await asyncio.sleep(0.2)
            continue

        if flight_completed:
            await asyncio.sleep(0.2)
            continue

        # Read full CSV in advance
        with open(CSV_PATH, newline='') as csvfile:
            reader = list(csv.DictReader(csvfile))
            if not reader: continue
            t0 = float(reader[0]['timestamp'])
            replay_start = asyncio.get_event_loop().time()
            for i, row in enumerate(reader):
                now = asyncio.get_event_loop().time()
                t_target = float(row['timestamp']) - t0
                elapsed = now - replay_start
                to_wait = t_target - elapsed
                if to_wait > 0:
                    await asyncio.sleep(to_wait)
                data = {
                    "timestamp": float(row["timestamp"]),
                    "altitude": float(row["altitude"]),
                    "velocity": float(row["velocity"]),
                    "acceleration": float(row["acceleration"]),
                    "roll": float(row["roll"]),
                    "pitch": float(row["pitch"]),
                    "yaw": float(row["yaw"]),
                    "lat": float(row["latitude"]),
                    "lon": float(row["longitude"]),
                }
                await ws.send_json(data)
            # after one full flight
            await ws.send_json({"done": True})
            flight_completed = True
            status["launched"] = False  # Reset launch status
            await asyncio.sleep(1.0)
