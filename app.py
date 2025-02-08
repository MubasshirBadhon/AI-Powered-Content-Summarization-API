from flask import Flask, request, jsonify, abort
from transformers import pipeline
import os

app = Flask(__name__)

# Load the summarization pipeline from Hugging Face Transformers
summarizer = pipeline("summarization")

# Set a dummy API key for demonstration purposes
API_KEY = "your_secret_api_key"

def validate_api_key(api_key):
    """Validate the provided API key."""
    return api_key == API_KEY

@app.route('/summarize', methods=['POST'])
def summarize():
    # Check for API key in headers
    api_key = request.headers.get('API-Key')
    if not validate_api_key(api_key):
        abort(403, description="Invalid API key")

    # Get the text content from the request
    data = request.json
    if not data or 'text' not in data:
        abort(400, description="Invalid input: 'text' field is required")

    text = data['text']

    try:
        # Summarize the text
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        summarized_text = summary[0]['summary_text']

        # Return the summarized text in JSON format
        return jsonify({"summary": summarized_text})

    except Exception as e:
        # Handle any errors that occur during summarization
        abort(500, description=f"Summarization failed: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
