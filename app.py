from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    name = "Your Full Name"  # Replace with your full name
    username = os.getlogin()
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime())
    top_output = subprocess.check_output(['top', '-bn1']).decode('utf-8')

    # Create response for /htop endpoint
    return f"""
    <h1>System Information</h1>
    <p><b>Name:</b> {name}</p>
    <p><b>Username:</b> {username}</p>
    <p><b>Server Time (IST):</b> {server_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
