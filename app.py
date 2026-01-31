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
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

prompt = f"""
You are an expert hackathon mentor.

Given these raw notes:
{notes}

Do the following:
1. Create a clear execution plan
2. Suggest features to keep
3. Suggest features to cut
4. Generate a README draft

Return the output in JSON format with keys:
plan, features_to_keep, features_to_cut, readme
"""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

output = response.choices[0].message.content
if __name__ == "__main__":
    app.run(debug=True)
