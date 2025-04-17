document.getElementById('uploadForm').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const fileInput = document.getElementById('fileInput');
    const file = fileInput.files[0];
    
    if (!file) {
        showError('Please select a file');
        return;
    }
    
    const formData = new FormData();
    formData.append('file', file);
    
    // Show loading state
    document.getElementById('loading').style.display = 'block';
    document.getElementById('results').style.display = 'none';
    document.getElementById('error').style.display = 'none';
    
    try {
        const response = await fetch('/upload', {
            method: 'POST',
            body: formData
        });
        
        const data = await response.json();
        
        if (response.ok) {
            // Display results
            displayResults(data);
        } else {
            showError(data.error || 'An error occurred while processing your file');
        }
    } catch (error) {
        showError('An error occurred while uploading the file');
    } finally {
        document.getElementById('loading').style.display = 'none';
    }
});

function displayResults(data) {
    // Display plots
    const timeSeriesPlot = JSON.parse(data.time_series_plot);
    const powerSpectrumPlot = JSON.parse(data.power_spectrum_plot);
    
    Plotly.newPlot('timeSeriesPlot', timeSeriesPlot.data, timeSeriesPlot.layout);
    Plotly.newPlot('powerSpectrumPlot', powerSpectrumPlot.data, powerSpectrumPlot.layout);
    
    // Display dominant cycles
    const cyclesTableBody = document.getElementById('cyclesTableBody');
    cyclesTableBody.innerHTML = '';
    
    data.dominant_cycles.forEach(cycle => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${cycle.period.toFixed(2)}</td>
            <td>${cycle.strength.toExponential(2)}</td>
        `;
        cyclesTableBody.appendChild(row);
    });
    
    document.getElementById('results').style.display = 'block';
}

function showError(message) {
    const errorDiv = document.getElementById('error');
    errorDiv.textContent = message;
    errorDiv.style.display = 'block';
} 