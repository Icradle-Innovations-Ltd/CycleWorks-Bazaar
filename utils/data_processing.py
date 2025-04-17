import numpy as np
from scipy.fft import fft
import pandas as pd

def process_stock_data(df):
    """
    Process stock data to extract time series, compute FFT, and identify dominant cycles.
    
    Args:
        df (pd.DataFrame): DataFrame containing 'date' and 'price' columns
        
    Returns:
        tuple: (time_series, power_spectrum, dominant_cycles)
    """
    # Ensure required columns exist
    if not all(col in df.columns for col in ['date', 'price']):
        raise ValueError("CSV must contain 'date' and 'price' columns")
    
    # Convert date to datetime and sort
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values('date')
    
    # Extract time series data
    time_series = df['price'].values
    
    # Compute FFT
    n = len(time_series)
    fft_result = fft(time_series)
    
    # Compute power spectrum (magnitude squared)
    power_spectrum = np.abs(fft_result) ** 2
    
    # Get sampling frequency (assuming daily data)
    sampling_freq = 1  # 1/day
    
    # Find dominant cycles
    frequencies = np.fft.fftfreq(n, d=1/sampling_freq)
    positive_freq_mask = frequencies > 0
    frequencies = frequencies[positive_freq_mask]
    power_spectrum = power_spectrum[positive_freq_mask]
    
    # Get top 5 dominant cycles
    top_indices = np.argsort(power_spectrum)[-5:][::-1]
    dominant_cycles = []
    
    for idx in top_indices:
        freq = frequencies[idx]
        period = 1/freq if freq != 0 else float('inf')
        strength = power_spectrum[idx]
        dominant_cycles.append({
            'period': period,
            'strength': strength
        })
    
    return time_series, power_spectrum, dominant_cycles 