import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Python Monitoring Application is Running!"

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "message": "Application is working"
    })

@app.route("/system")
def system_info():

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    return jsonify({
        "CPU Usage": cpu,
        "Memory Usage": memory,
        "Disk Usage": disk
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
