from flask_cors import CORS
from flask import Flask, request, jsonify
from routes import routes

app = Flask(__name__)
app.register_blueprint(routes)
CORS(app,origins=["http://localhost:5050"])

