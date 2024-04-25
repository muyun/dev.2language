from flask import Flask, render_template, request, jsonify

import llm

def get_conversation(
        prompt, 
        model=llm.get_model("orca-mini-3b-gguf2-q4_0"),
        system = "Answer like a very friendly AI agent to provide youth emotional support",
        ):
    conv = model.conversation()
    response = conv.prompt(prompt, system=system)
    return response.text()

# Initializing flask app
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route('/get')
def get_messages():
    userText = request.args.get('msg')
    response = get_conversation(userText)
    #print(response)
    return response

     
# Running app
if __name__ == '__main__':
    app.run(port=5000, debug=True)