from flask_cors import CORS
from flask import Flask, request, jsonify
from routes import routes
import os
print(os.getenv("FLASK_ENV"))
app = Flask(__name__)
app.register_blueprint(routes)
CORS(app,origins=["*"])

if __name__ == '__main__':
    app.run()

