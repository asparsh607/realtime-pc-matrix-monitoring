from flask import Flask, render_template
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import psutil
import time
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_plot')
def update_plot():
    cpu_percent = psutil.cpu_percent()
    memory_percent = psutil.virtual_memory().percent
    current_time = time.strftime("%H:%M:%S")
    disc_usage_c = psutil.disk_usage('C:/')._asdict()
    disc_usage_d = psutil.disk_usage('D:/')._asdict()

    return {
        'cpu_percent': cpu_percent,
        'memory_percent': memory_percent,
        'current_time': current_time,
        'disc_usage_c' : disc_usage_c,
        'disc_usage_d' : disc_usage_d
    }

if __name__ == '__main__':
    app.run(debug=True)
