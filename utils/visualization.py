import plotly.graph_objects as go
import numpy as np
import json

def create_visualizations(time_series, power_spectrum):
    """
    Create interactive visualizations for time series and power spectrum.
    
    Args:
        time_series (np.ndarray): Time series data
        power_spectrum (np.ndarray): Power spectrum data
        
    Returns:
        tuple: (time_series_plot_json, power_spectrum_plot_json)
    """
    # Create time series plot
    time_series_fig = go.Figure()
    time_series_fig.add_trace(go.Scatter(
        y=time_series,
        mode='lines',
        name='Stock Price',
        line=dict(color='blue')
    ))
    time_series_fig.update_layout(
        title='Stock Price Time Series',
        xaxis_title='Time (days)',
        yaxis_title='Price',
        template='plotly_white'
    )
    
    # Create power spectrum plot
    power_spectrum_fig = go.Figure()
    power_spectrum_fig.add_trace(go.Scatter(
        y=power_spectrum,
        mode='lines',
        name='Power Spectrum',
        line=dict(color='red')
    ))
    power_spectrum_fig.update_layout(
        title='Power Spectrum',
        xaxis_title='Frequency (1/day)',
        yaxis_title='Power',
        template='plotly_white'
    )
    
    # Convert figures to JSON
    time_series_plot_json = json.dumps(time_series_fig, cls=plotly.utils.PlotlyJSONEncoder)
    power_spectrum_plot_json = json.dumps(power_spectrum_fig, cls=plotly.utils.PlotlyJSONEncoder)
    
    return time_series_plot_json, power_spectrum_plot_json 