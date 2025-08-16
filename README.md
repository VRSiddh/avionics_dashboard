# 🚀 Rocket Avionics Dashboard

A real-time rocket flight monitoring dashboard with live telemetry data visualization, built with FastAPI backend and HTML, CSS, Javascript for the frontend.

![Dashboard Preview](https://img.shields.io/badge/Status-Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68+-green)
![Chart.js](https://img.shields.io/badge/Chart.js-4.3.3-orange)

## ✨ Features

- **Real-time Telemetry**: Live data streaming via WebSocket
- **Interactive Charts**: Altitude, velocity, acceleration, and attitude visualization
- **Flight Timer**: Precise mission timing with tenths of a second accuracy
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile
- **Sci-fi UI**: Modern futuristic interface with glassmorphism effects
- **Single Flight Simulation**: CSV-based flight data replay
- **Status Monitoring**: Real-time connection and flight status indicators

## 📊 Dashboard Components

- **Altitude Chart**: Real-time altitude tracking in meters
- **Velocity Chart**: Speed monitoring in m/s
- **Acceleration Chart**: G-force and acceleration data
- **Euler Angles**: Roll, pitch, and yaw visualization
- **Data Table**: Live parameter readouts
- **Flight Timer**: Mission elapsed time
- **Control Panel**: Connect, launch, disconnect, and reset functions

## 🛠️ Technology Stack

### Backend
- **FastAPI**: High-performance web framework
- **WebSocket**: Real-time bidirectional communication
- **Python 3.8+**: Modern Python with async support

### Frontend
- **HTML5**: Semantic markup
- **CSS3**: Advanced styling with CSS Grid and Flexbox
- **JavaScript (ES6+)**: Modern JavaScript with async/await
- **Chart.js**: Interactive data visualization
- **Google Fonts**: Orbitron and Share Tech Mono for sci-fi aesthetics

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/rocket-avionics-dashboard.git
   cd rocket-avionics-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python main.py
   ```

4. **Access the dashboard**
   - Open `index.html` in your web browser
   - Or serve it using a local server: `python -m http.server 8080`
   - Navigate to `http://localhost:8080`

## 🚀 Usage

### Starting the Mission

1. **Connect**: Click "Connect" to establish connection with flight controller
2. **Launch**: Click "Launch" to start the flight simulation
3. **Monitor**: Watch real-time data on charts and data table
4. **Reset**: Click "Reset" to clear all data and start fresh

### Flight Data

The dashboard reads flight data from `abhyuday_flight.csv` which contains:
- Timestamp
- Altitude (meters)
- Velocity (m/s)
- Acceleration (m/s²)
- Roll, Pitch, Yaw (degrees)
- Latitude, Longitude (GPS coordinates)

## 📁 Project Structure

```
rocket-avionics-dashboard/
├── main.py                 # FastAPI backend server
├── index.html             # Main dashboard interface
├── abhyuday_flight.csv    # Flight telemetry data
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## 🔧 API Endpoints

- `POST /api/connect` - Establish flight controller connection
- `POST /api/disconnect` - Disconnect from flight controller
- `POST /api/launch` - Initiate rocket launch
- `POST /api/reset` - Reset all system states
- `GET /api/status` - Get current connection status
- `WS /ws/telemetry` - WebSocket for real-time telemetry data

## 🎨 Customization

### Styling
The dashboard uses CSS custom properties for easy theming:
```css
:root {
  --accent: #18ffea;
  --green: #00f7a4;
  --danger: #ff3870;
  --orange: #ffde38;
}
```

### Chart Configuration
Modify chart options in the JavaScript section:
```javascript
function baseChartOptions(unit) {
  return {
    responsive: true,
    plugins: { legend: { display: false } },
    scales: {
      x: { ticks: { display: false } },
      y: { grid: { color: "rgba(255,255,255,0.1)" } }
    }
  }
}
```

## 📱 Responsive Design

The dashboard is fully responsive with breakpoints:
- **Desktop**: 1200px+
- **Tablet**: 768px - 1199px
- **Mobile**: 320px - 767px

## 🔍 Troubleshooting

### Common Issues

1. **WebSocket Connection Failed**
   - Ensure the backend server is running
   - Check if port 8000 is available
   - Verify firewall settings

2. **Charts Not Updating**
   - Check browser console for JavaScript errors
   - Ensure Chart.js CDN is loading properly
   - Verify WebSocket connection status

3. **Flight Data Not Loading**
   - Confirm `abhyuday_flight.csv` exists in project root
   - Check CSV file format and data integrity
   - Verify file permissions

### Debug Mode

Enable debug logging by adding to browser console:
```javascript
localStorage.setItem('debug', 'true');
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **FastAPI** for the high-performance backend
- **Chart.js** for beautiful data visualization
- **Google Fonts** for the sci-fi typography
- **CSS Grid & Flexbox** for responsive layouts

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the browser console for error messages

---

**Made with ❤️ for the aerospace community** 