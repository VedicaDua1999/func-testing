from flask import Flask, Response
import azure.functions as func
import os
import logging


app = Flask(__name__)

@app.route('/')
def hello():
    return f"""
    <h1>🚀 Dummy Python App</h1>
    <p>Build ID: {os.environ.get('BUILD_ID', 'local')}</p>
    <p>Image Tag: {os.environ.get('IMAGE_TAG', 'latest')}</p>
    <p>Container App: Ready! ✅</p>
    """

def main(req: func.HttpRequest) -> func.HttpResponse:
    # return func.WsgiMiddleware(app).handle(req, req.context) 
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse("Hello from Functions!", status_code=200)

