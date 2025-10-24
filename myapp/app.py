from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat.chat import get_response
import os

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("base.html")  # đổi PHP sang HTML

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data.get("message", "")
    selected_product = data.get("selected_product", "")

    if selected_product:
        response = f"Bạn đã chọn: {selected_product}"
    else:
        response = get_response(text)

    return jsonify({"answer": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
