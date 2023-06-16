from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load health-data.json
with open('health-data.json') as file:
    health_data = json.load(file)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    return get_Chat_response(msg)

def get_Chat_response(text):
    # Check if the user's input matches any diseases in the health data
    with open('health-data.json') as file:
        data = json.load(file)
        diseases = data['diseases']
        for disease in diseases:
            if text.lower() in disease['name'].lower():
                return disease['description']
           
            
    return "I'm sorry, but I couldn't find information about that disease."

if __name__ == '__main__':
    app.run()
