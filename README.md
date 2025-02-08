# AI-Powered-Content-Summarization-API
Install the required libraries: pip install flask transformers.
Run the application: python app.py.
The API will be available at http://127.0.0.1:5000/summarize.

Test the endpoint using a tool like curl or Postman:
curl -X POST http://127.0.0.1:5000/summarize \
     -H "Content-Type: application/json" \
     -H "API-Key: your_secret_api_key" \
     -d '{"text": "Your long text to summarize goes here."}'

Functional REST API for text summarization with security and error handling.
