import os
import base64
from flask import Flask, render_template, request, jsonify
from groq import Groq
from dotenv import load_dotenv  # <-- add this

load_dotenv()  # <-- load .env variables

app = Flask(__name__)

GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    image = request.files['image']
    text_query = request.form['query']

    encoded_image = base64.b64encode(image.read()).decode('utf-8')

    messages = [
        {
            "role": "user",
            "content": [
                {"type": "text", "text": text_query},
                {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{encoded_image}"}},
            ],
        }
    ]

    model = "meta-llama/llama-4-scout-17b-16e-instruct"
    response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    result = response.choices[0].message.content
    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True)


# print(chat_completion.choices[0].message.content)
