# CycleWorks - Stock Market Signal Processing

A web application that analyzes stock market data using Fourier Transforms to identify periodic patterns and cycles in price movements.

## Features

- Upload CSV files containing stock price data
- Visualize time series data
- Perform Fast Fourier Transform (FFT) analysis
- Identify dominant cycles in the data
- Interactive visualizations using Plotly

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Icradle-Innovations-Ltd/CycleWorks-Bazaar.git
cd CycleWorks-Bazaar
```

2. Create and activate a virtual environment:

On Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

3. Install the required packages:
```bash
python -m pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

## Project Structure

```
CycleWorks-Bazaar/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── sample_data.csv        # Sample stock data
├── static/                # Static assets
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── main.js       # Client-side JavaScript
├── templates/            # HTML templates
│   └── index.html       # Main page template
└── utils/               # Utility modules
    ├── data_processing.py  # Data processing logic
    └── visualization.py    # Visualization functions
```

## Running the Application

1. Make sure your virtual environment is activated

2. Start the Flask server:
```bash
python app.py
```

3. Open your web browser and navigate to:
```
http://localhost:5000
```

## Using the Application

1. Prepare your data:
   - Create a CSV file with two columns: 'date' and 'price'
   - The date should be in YYYY-MM-DD format
   - The price should be a numerical value

2. Upload your data:
   - Click the "Choose File" button
   - Select your CSV file
   - Click "Analyze"

3. View the results:
   - Time series plot of your data
   - Power spectrum showing frequency components
   - Table of dominant cycles with their periods and strengths

## Sample Data

A sample CSV file (`sample_data.csv`) is included in the repository for testing purposes. It contains 30 days of sample stock price data.

## Troubleshooting

If you encounter any issues:

1. Make sure all dependencies are installed correctly
2. Check that your CSV file follows the required format
3. Ensure your virtual environment is activated
4. Verify that no other application is using port 5000

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Flask web framework
- NumPy and SciPy for numerical computations
- Plotly for interactive visualizations
- Bootstrap for UI components