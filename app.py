from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Second Brain is running"

@app.route("/organize", methods=["POST"])
def organize():
    data = request.json
    notes = data.get("notes", "")

    # Placeholder AI output
    output = {
        "plan": "Build MVP, test, demo",
        "features": ["Input notes", "AI organization", "Output plan"],
        "readme": "This project helps hackathon teams organize ideas."
    }

    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)
