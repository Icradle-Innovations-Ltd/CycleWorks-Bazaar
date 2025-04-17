from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from scipy.fft import fft
import plotly
import json
from utils.data_processing import process_stock_data
from utils.visualization import create_visualizations

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

ALLOWED_EXTENSIONS = {'csv'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the uploaded file
            df = pd.read_csv(filepath)
            time_series, power_spectrum, dominant_cycles = process_stock_data(df)
            
            # Create visualizations
            time_series_plot, power_spectrum_plot = create_visualizations(time_series, power_spectrum)
            
            # Clean up the uploaded file
            os.remove(filepath)
            
            return jsonify({
                'time_series_plot': time_series_plot,
                'power_spectrum_plot': power_spectrum_plot,
                'dominant_cycles': dominant_cycles
            })
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True) 