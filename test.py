from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>🚀 Dummy Python App</h1>
    <p>Build ID: {os.environ.get('BUILD_ID', 'local')}</p>
    <p>Image Tag: {os.environ.get('IMAGE_TAG', 'latest')}</p>
    <p>Container App: Ready! ✅</p>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081)
