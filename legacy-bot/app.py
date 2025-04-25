# legacy_bot/app.py

from flask import Flask, request, jsonify
from flasgger import Swagger
import requests
import time

app = Flask(__name__)
swagger = Swagger(app)

def call_ai_service(question) :
    url = "http://ai-brain:8000/ask"
    max_retries = 5

    for attempt in range(max_retries):
        try:
            response = requests.post(url, json={"question": question})
            return response.json()
        except requests.exceptions.ConnectionError as e:
            print("[Attempt %d] AI service not ready, retrying in 2s..." % (attempt + 1))
            time.sleep(2)
        except Exception as e:
            print("Unexpected error: %s" % str(e))
            break
    return {"response": "AI service unavailable after retries."}

@app.route('/ask', methods = ['POST'])
def ask():
    """
        Ask a question to the AI bot
        ---
        parameters:
          - name: question
            in: body
            type: string
            required: true
            description: The user's question
            schema:
              type: object
              properties:
                question:
                  type: string
        responses:
          200:
            description: Bot response
            schema:
              type: object
              properties:
                response:
                  type: string
        """
    data = request.get_json()
    question = data.get('question')
    return jsonify(call_ai_service(question))

@app.route('/health', methods = ['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
