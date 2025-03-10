from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS

app = Flask(__name__, static_folder="frontend")
CORS(app)  # Enable CORS to allow frontend requests

@app.route("/")
def home():
    return jsonify({"message": "Hello, World!"})

@app.route("/templates")
def serve_frontend():
    return send_from_directory("frontend", "index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
