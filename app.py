from flask import Flask, render_template, request
import chatbot  

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["GET"])
def get_bot_response():
    user_input = request.args.get("msg")
    intent = chatbot.recognize_intent(user_input)
    if intent != "unknown":
        return chatbot.responses[intent]
    else:
        return "I'm sorry, I didn't understand that. Transferring to human support..."

if __name__ == "__main__":
    app.run(debug=True)
