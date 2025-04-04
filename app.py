from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import logging

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication.

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# FIFO Page Replacement Algorithm
def fifo(pages, frames):
    page_faults, memory = 0, []
    result = []

    for page in pages:
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                memory.pop(0)
                memory.append(page)
                page_faults += 1
            result.append(memory[:])  # Store current memory state

    return {"faults": page_faults, "states": result}

# Home Route (renders the HTML page)
@app.route("/")
def home():
    return render_template("index.html")

# API Route to Process Requests
@app.route("/simulate", methods=["POST"])
def simulate():
    data = request.json
    logging.info(f"Received request with data: {data}")
    pages = data.get("pages", [])
    frames = data.get("frames", 3)

    result = fifo(pages, frames)
    logging.info(f"Simulation result: {result}")
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
