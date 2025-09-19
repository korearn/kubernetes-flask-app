from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return f'🚀 ¡Mi primera app Dockerizada! | Hostname: {os.uname().nodename}'

@app.route('/health')
def health():
    return '✅ Healthy'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
