from flask import Flask
import socket

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Advanced AWS DevOps Project!"

@app.route("/health")
def health():
    return {"status": "UP"}

@app.route("/version")
def version():
    return {"version": "v1.0", "host": socket.gethostname()}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
