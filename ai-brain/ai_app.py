# ai-brain/ai_app.py

from flask import Flask, request, jsonify
from flasgger import Swagger

ai_app = Flask(__name__)
swagger = Swagger(ai_app)

@ai_app.route("/ask", methods=["POST"])
def ask() :
    """
     Ask something to the AI brain.
     ---
     parameters:
       - name: body
         in: body
         required: true
         schema:
           type: object
           properties:
             question:
               type: string
     responses:
       200:
         description: AI-generated response
         schema:
           type: object
           properties:
             response:
               type: string
     """
    data = request.get_json(force=True)
    question = data["question"]
    return jsonify({'response': f'Ai powered soon {question}'})

@ai_app.route('/health', methods = ['GET'])
def health():
    return jsonify({'status': 'ok'}), 200

if __name__ == "__main__":
    ai_app.run(host="0.0.0.0", port=8000, debug=True)