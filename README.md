---
title: Getaround Analytics Dashboard
emoji: 🚗
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: "1.29.0"
app_file: app.py
pinned: false
---

# 🚗 Getaround Analytics Dashboard

A comprehensive Streamlit dashboard for analyzing Getaround rental data, featuring interactive visualizations, buffer threshold simulations, and key performance indicators.

![Getaround Dashboard](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white)

## 📋 Table of Contents

- [Features](#-features)
- [Installation](#-installation)
- [Usage](#-usage)
- [Docker Setup](#-docker-setup)
- [Data Requirements](#-data-requirements)
- [Dashboard Sections](#-dashboard-sections)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **Interactive Data Filtering**: Filter rentals by check-in type (mobile, connect, or both)
- **Key Performance Indicators**: Real-time metrics including total rentals, completion rates, and delay statistics
- **Buffer Threshold Simulation**: Analyze the impact of different time buffers between consecutive rentals
- **Modern UI Design**: Clean, responsive interface with Getaround's brand colors
- **Real-time Visualizations**: Interactive charts powered by Plotly
- **Data Refresh Capability**: Reload and refresh dashboard data on demand

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/Francescogiraldi/getaround.git
   cd getaround
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Prepare your data**
   - Ensure you have `processed_delay_getaround_data.csv` in the project directory
   - Or run the data processing script: `python processing_delay_analysis_data.py`

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the dashboard**
   - Open your browser and navigate to `http://localhost:8501`

## 🐳 Docker Setup

### Build and Run with Docker

1. **Build the Docker image**
   ```bash
   docker build -t getaround-dashboard .
   ```

2. **Run the container**
   ```bash
   docker run -p 8501:8501 getaround-dashboard
   ```

3. **Access the application**
   - Navigate to `http://localhost:8501` in your browser

### Docker Compose (Optional)

```yaml
version: '3.8'
services:
  getaround-dashboard:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
```

## 📊 Data Requirements

The dashboard expects a CSV file named `processed_delay_getaround_data.csv` with the following columns:

- `checkin_type`: Type of check-in (mobile/connect)
- `delay_at_checkout_in_minutes`: Delay time in minutes
- `previous_ended_rental_id`: ID of previous rental
- `time_delta_with_previous_rental_in_minutes`: Time gap between rentals
- `state`: Rental state (ended/canceled)

## 🎯 Dashboard Sections

### 1. Data Filters
- **Check-in Type Filter**: Filter data by mobile, connect, or both rental types
- **Refresh Button**: Reload and refresh dashboard data

### 2. Key Performance Indicators
- Total Rentals
- Completed Rentals with completion rate
- Canceled Rentals with cancellation rate
- Rentals with Delay
- Average and Median Delay times

### 3. Buffer Threshold Simulation
- Interactive slider to set buffer thresholds (0-720 minutes)
- Real-time impact analysis showing:
  - Percentage of rentals affected
  - Critical cases that would be solved
  - Potential cancellation prevention
- Interactive visualization of results

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualizations**: Plotly, Matplotlib
- **Styling**: Custom CSS with modern design principles
- **Containerization**: Docker

## 📁 Project Structure

```
getaround/
├── app.py                              # Main Streamlit application
├── processing_delay_analysis_data.py   # Data processing script
├── processed_delay_getaround_data.csv  # Processed data file
├── requirements.txt                    # Python dependencies
├── Dockerfile                         # Docker configuration
├── README.md                          # Project documentation
└── .gitignore                         # Git ignore rules
```

## 🎨 Design Features

- **Modern UI**: Clean, card-based layout with hover effects
- **Brand Colors**: Getaround's signature violet theme (#aa1ba3)
- **Responsive Design**: Optimized for desktop and mobile viewing
- **Interactive Elements**: Smooth transitions and modern styling
- **Accessibility**: Clear typography and intuitive navigation

## 🔧 Configuration

The application can be customized by modifying:

- **Colors**: Update CSS variables in `app.py`
- **Metrics**: Modify KPI calculations in the metrics section
- **Visualizations**: Customize Plotly charts for different insights
- **Filters**: Add additional filtering options

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Francesco Giraldi** - 2025

- GitHub: [@Francescogiraldi](https://github.com/Francescogiraldi)
- Project Link: [https://github.com/Francescogiraldi/getaround](https://github.com/Francescogiraldi/getaround)

## 🙏 Acknowledgments

- Getaround for the inspiration and data structure
- Streamlit community for the amazing framework
- Plotly for interactive visualizations

---

**Made with ❤️ by Francesco Giraldi 2025**