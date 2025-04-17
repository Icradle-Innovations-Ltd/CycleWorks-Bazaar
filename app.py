from flask import Flask, render_template, request, jsonify
import os
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from scipy.fft import fft
import plotly.graph_objects as go
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
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if not allowed_file(file.filename):
            return jsonify({'error': 'Invalid file type. Please upload a CSV file.'}), 400
        
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            # Process the uploaded file
            df = pd.read_csv(filepath)
            
            # Validate required columns
            if not all(col in df.columns for col in ['date', 'price']):
                return jsonify({'error': 'CSV must contain "date" and "price" columns'}), 400
            
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
            
        except pd.errors.EmptyDataError:
            return jsonify({'error': 'The uploaded file is empty'}), 400
        except pd.errors.ParserError:
            return jsonify({'error': 'Error parsing CSV file'}), 400
        except Exception as e:
            return jsonify({'error': f'Error processing file: {str(e)}'}), 500
        finally:
            # Ensure file is removed even if an error occurs
            if os.path.exists(filepath):
                os.remove(filepath)
                
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True) 