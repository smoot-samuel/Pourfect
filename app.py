from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def index():
    return "Pourfect backend is running!"

@app.route("/api/predict")
def predict():
    today = datetime.now()
    prediction = []
    for i in range(14):
        date = (today + timedelta(days=i)).strftime("%Y-%m-%d")
        prediction.append({
            "date": date,
            "GreyGoose": 3 + (i % 3),
            "DonJulio": 2 + ((i + 1) % 2),
            "Meiomi": 1 + ((i + 2) % 2)
        })
    return jsonify({"status": "success", "data": prediction})

if __name__ == "__main__":
    app.run(debug=True)