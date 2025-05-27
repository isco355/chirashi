from flask_cors import CORS
from flask import Flask, request, jsonify
from routes import routes
import os
print(os.getenv("FLASK_ENV"))
app = Flask(__name__)
app.register_blueprint(routes)
CORS(app,origins=["*"])
# Configure the upload folder
UPLOAD_FOLDER = 'uploads'  # Directory to save uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
if __name__ == '__main__':
    app.run()

