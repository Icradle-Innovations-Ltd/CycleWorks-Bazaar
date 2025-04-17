```python
# The Bazaar: CycleWorks

Project Repository: https://github.com/Icradle-Innovations-Ltd/CycleWorks-Bazaar.git

Group Members:
Amanya Peter – 2024bcs033@std.must.ac.ug
Doreen Miracle – 2024bcs130@std.must.ac.ug
Twinomugisha Nickson – 2024bcs168@std.must.ac.ug
Asiimwe Shabellah – 2024BCS049@std.must.ac.ug
Kangwagye Jonas – 2024BCS194@std.must.ac.ug
Amon Muhwezi – 2024BCS109@std.must.ac.ug
Maro Edly – 2024BCS097@std.must.ac.ug
Nanjuki Daphine – 2024BCS129@std.must.ac.ug
Rwendeire Joshua Truth – 2024BCS148@std.must.ac.ug
Katusiime Moreen – 2024bcs084@std.must.ac.ug

# Stock Market Signal Processing Web App (CycleWorks)

## Setup and Installation

### Prerequisites
- Python 3.11 or higher (Python 3.13 recommended)
- pip (Python package installer)

### Installation Steps

1. Clone the repository:
```bash
git clone https://github.com/Icradle-Innovations-Ltd/CycleWorks-Bazaar.git
cd CycleWorks-Bazaar
```

2. Create and activate a virtual environment:

For Windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

For Linux/Mac:
```bash
python -m venv venv
source venv/bin/activate
```

3. Upgrade pip and install build tools:
```bash
python -m pip install --upgrade pip setuptools wheel
```

4. Install the required packages:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Upload a CSV file containing stock price data with the following format:
```csv
date,price
2023-01-01,100.0
2023-01-02,101.5
...
```

### Testing the Application

You can test the application using the provided `sample_data.csv` file in the project root directory.

## Project Structure

The project is organized as a Flask-based web application with distinct frontend and backend components:

```python
stock-market-signal-processing/
├── app.py                  # Main Flask application
├── requirements.txt        # Python dependencies
├── static/                # Static assets
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── main.js       # Client-side JavaScript
├── templates/            # HTML templates
│   └── index.html       # Main page template
└── utils/               # Utility modules
    ├── data_processing.py  # Data loading and FFT logic
    └── visualization.py    # Plotly visualization generation
```

## Features

1. **Stock Data Analysis**: 
   - Upload CSV files containing stock price data
   - Process data using Fast Fourier Transform (FFT)
   - Identify dominant cycles in stock price movements

2. **Interactive Visualizations**:
   - Time series plot of stock prices
   - Power spectrum plot showing frequency components
   - Table of dominant cycles with periods and strengths

3. **User-Friendly Interface**:
   - Clean, modern design using Bootstrap
   - Responsive layout for different screen sizes
   - Interactive plots using Plotly

## Troubleshooting

If you encounter any issues during installation:

1. Ensure you have the correct Python version installed
2. Try installing packages one by one:
```bash
pip install flask==2.3.3
pip install numpy>=2.0.0
pip install scipy>=1.11.4
pip install pandas>=2.2.0
pip install plotly>=5.18.0
pip install python-dotenv>=1.0.0
```

3. If you're using Python 3.13 and encounter build issues, consider:
   - Installing Microsoft Visual C++ Build Tools
   - Or downgrading to Python 3.11/3.12

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Define Clear Objectives

The Stock Market Signal Processing web app is designed with the following objectives:

1. **Analyze Stock Price Data**: Utilize Fourier Transforms to detect periodic patterns or cycles in historical stock price data, helping users identify recurring market trends.
2. **Visualize Insights**: Offer interactive visualizations of the time series data and its power spectrum, making it easier for users to interpret frequency components and market behavior.
3. **Educate Users**: Act as an educational tool to teach signal processing techniques applied to financial data, with a focus on understanding Fourier Transforms and their relevance to stock market cycles.

This application solves the problem of making complex signal processing accessible to learners and enthusiasts interested in financial data analysis.

## Plan the Development Process

### Research

- **Theoretical Concepts**: Investigate Fourier Transform fundamentals, focusing on how they decompose time series data into frequency components, and their specific application to stock price analysis.

- **Existing Solutions**: Review tools or libraries (e.g., TA-Lib, QuantLib) that perform stock market analysis using signal processing, identifying gaps the project can address.

### Design

- **Architecture**: Build a web application with Flask as the backend to process data and serve results, paired with Plotly for interactive frontend visualizations.

- **User Interface**: Develop a simple, user-friendly interface allowing users to upload CSV files containing stock data (with "date" and "price" columns) and view analysis results.

### Implementation

- **Modular Code**: Structure the codebase into distinct modules:
  - Data processing (e.g., loading CSV files, applying FFT)
  - Visualization (e.g., generating time series and power spectrum plots)
  - Web routing (e.g., Flask routes for handling uploads and displaying results)
- **Clear Documentation**: Include inline code comments explaining key steps (e.g., FFT computation) and a project report summarizing the development process.

### Testing

- **Validation**: Test the app with diverse stock price datasets to confirm accurate detection of cycles and patterns.

- **Edge Cases**: Handle scenarios like missing data, non-numeric inputs, or irregular time intervals, ensuring robust performance.

## Use Appropriate Tools

### Programming Languages

- **Python**: Chosen as the core language due to its versatility, extensive library ecosystem, and suitability for data analysis and web development.

### Libraries

- **NumPy**: Used for numerical computations, including the Fast Fourier Transform (FFT) to analyze frequency components.

- **SciPy**: Provides advanced signal processing capabilities, enhancing FFT implementation.

- **Pandas**: Facilitates reading and manipulating CSV files containing stock data.

- **Plotly**: Preferred over Matplotlib for its interactive visualization features, enabling users to explore time series and power spectra dynamically.

- **Flask**: A lightweight web framework to manage backend logic, such as processing uploaded files and rendering results.

**Note**: While libraries like pyaudio, scikit-image, scikit-learn, or TensorFlow are powerful, they are not directly relevant to this project's scope, which focuses on signal processing and visualization rather than audio, image processing, or machine learning.

## Document the Process

### Project Report

Create a comprehensive document detailing:
- **Learning Journey**: Insights gained about Fourier Transforms and their financial applications.

- **Challenges Faced**: Issues like handling irregular time series data or interpreting noisy frequency spectra.

- **Solutions Implemented**: Techniques such as data interpolation for missing values or detrending to remove long-term trends before FFT analysis.

- **Code Comments**: Embed clear, concise comments within the code to explain functionality, making it reusable and understandable for others.

## Collaborate and Share

- **Teamwork**: Encourage collaboration by dividing tasks (e.g., one person focuses on data processing, another on visualization) if working in a group.

- **Version Control**: Utilize Git for tracking changes, managing contributions, and maintaining a project history. Host the repository on platforms like GitHub to share ideas and code with others.

## Additional Considerations

- **Data Assumptions**: The app expects CSV files with "date" and "price" columns. Users should be informed of this format for smooth operation.

- **Optional Enhancements**: Future iterations could include detrending the time series, integrating real-time stock data APIs (e.g., Yahoo Finance), or adding educational tooltips about signal processing concepts.

This approach ensures the Stock Market Signal Processing web app meets the guidelines, delivering a functional, educational, and well-documented tool for analyzing stock market data.

This document outlines the project structure, use cases, tools, and implementation details for a web application that processes stock market data using signal processing techniques.

## Use Cases

The web app supports the following user interactions:

1. **Upload Stock Data**

   - Users upload a CSV file with "date" and "price" columns containing historical stock data.

2. **Visualize Time Series**

   - Users view an interactive plot of stock prices over time.

3. **Analyze Frequency Components**

   - Users see the power spectrum of the stock data, highlighting dominant cycles.

4. **Interpret Results**

   - Users receive a list of top dominant cycles (periods and strengths) for market analysis.

## Tools and Libraries

The following tools and libraries are required:

- **Python 3.x**: Core programming language.
- **Flask**: Web framework for building the app.
- **NumPy**: Numerical computations, including FFT.
- **SciPy**: Signal processing capabilities (FFT module).
- **Pandas**: CSV file handling and data manipulation.
- **Plotly**: Interactive visualizations.
- **Git**: Version control system.

## Implementation Details

### 1. Development Environment Setup

- Install Python 3.x.
- Create a virtual environment: `python -m venv venv`.
- Install dependencies: `pip install -r requirements.txt`.

### 2. Backend Development

- **data_processing.py**:
  - Load CSV using Pandas.
  - Compute FFT with NumPy/SciPy.
  - Calculate power spectrum and extract dominant frequencies.
- **visualization.py**:
  - Generate Plotly plots for time series and power spectrum.
- **app.py**:
  - Define routes (`/` for upload, `/results` for display).
  - Handle file uploads and integrate with utility modules.

### 3. Frontend Development

- **index.html**: Form for uploading CSV files.
- **results.html**: Displays plots and analysis results.
- **style.css**: Styles the UI for a clean look.
- **main.js**: Enhances interactivity (e.g., Plotly plot features).

### 4. Testing

- **Unit Tests**: Validate data processing and visualization functions.
- **Integration Tests**: Ensure end-to-end workflow (upload to display).
- **Edge Cases**: Handle malformed CSVs or missing data.

### 5. Additional Considerations

- **Data Validation**: Check CSV format and required columns.
- **Error Handling**: Display user-friendly error messages.
- **Performance**: Optimize FFT for large datasets.
- **Security**: Prevent malicious file uploads.
- **UX**: Provide clear instructions and feedback.

## Sample Requirements.txt

```python
flask==2.3.3
numpy==1.26.0
scipy==1.11.4
pandas==2.2.0
plotly==5.18.0
```