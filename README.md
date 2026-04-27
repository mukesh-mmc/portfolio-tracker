# 📊 Mutual Fund Portfolio Tracker

A modern, user-friendly web application built with Streamlit to track and analyze your mutual fund portfolio in real-time. This app fetches the latest Net Asset Values (NAV) from the MF API and provides comprehensive portfolio insights including performance metrics, allocation charts, and detailed breakdowns.

## ✨ Features

- **Real-time NAV Updates**: Automatically fetches current and historical NAV data from the MF API
- **Excel Integration**: Upload your portfolio data via Excel files for seamless import
- **SIP Support**: Automatic processing of Systematic Investment Plans with historical NAV calculations
- **Performance Metrics**: View total portfolio value, daily changes, returns, and XIRR calculations
- **Visual Analytics**: Interactive pie charts for portfolio allocation and matplotlib-based visualizations
- **Caching System**: Efficient caching of NAV data to reduce API calls and improve performance
- **Responsive Design**: Clean, wide-layout interface optimized for desktop and mobile viewing

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- macOS/Linux/Windows

### Setup Steps

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mukesh-mmc/portfolio-tracker.git
   cd portfolio-tracker
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **(Optional) Install Watchdog for better performance:**
   ```bash
   pip install watchdog
   ```

## 📖 Usage

1. **Start the application:**
   ```bash
   streamlit run app.py
   ```

2. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

3. **Upload your portfolio:**
   - Prepare an Excel file with your mutual fund holdings
   - Upload the file using the file uploader
   - Click "Run Portfolio Update" to fetch latest NAV data

4. **View results:**
   - See key metrics at the top
   - Browse the detailed portfolio table
   - Analyze allocation with the pie chart

### Excel File Format
Your Excel file should contain columns for:
- Scheme Name
- Scheme Code
- Units Held
- Purchase Price (optional)
- Purchase Date (optional)

### SIP (Systematic Investment Plan) Handling
The app supports automatic SIP processing to track your regular investments:

1. **Create a SIP Sheet**: Add a new sheet named "SIP" in your Excel file
2. **SIP Sheet Format**: Include the following columns:
   - Scheme Name: Name of the mutual fund scheme
   - Scheme Code: The unique code of the scheme
   - Day: The day of the month for SIP (e.g., 1 for 1st, 15 for 15th)
   - Amount: Monthly investment amount in rupees

3. **Automatic Processing**: When you upload the file and run the portfolio update, the app will:
   - Calculate SIP transactions for the current and previous month
   - Fetch NAV data for the SIP dates
   - Add new SIP entries to your portfolio if not already present
   - Adjust dates to working days if the SIP day falls on a weekend/holiday

**Example SIP Sheet:**

| Scheme Name | Scheme Code | Day | Amount |
|-------------|-------------|-----|--------|
| HDFC Top 200 Fund | 100123 | 1 | 5000 |
| SBI Bluechip Fund | 103504 | 15 | 3000 |

**Note**: SIP transactions are added automatically but won't duplicate existing entries.

- streamlit
- pandas
- requests
- openpyxl
- matplotlib
- watchdog (optional, for improved file watching)

## 🔧 Configuration

- The app uses the MF API (https://api.mfapi.in/) for NAV data
- NAV data is cached to minimize API requests
- Use the "Refresh NAV" button to clear cache and force fresh data

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Mukesh Kumar**
- GitHub: [@mukesh-mmc](https://github.com/mukesh-mmc)

---

*Built with ❤️ using Streamlit and Python*</content>
<parameter name="filePath">/Users/mukeshkumar/Documents/GitHub/portfolio-tracker/README.md