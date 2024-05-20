from flask import Flask, render_template, request
from ctransformers import AutoModelForCausalLM

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greet', methods=['POST'])
def greet():

    llm = AutoModelForCausalLM.from_pretrained("TheBloke/Mistral-7B-v0.1-GGUF", model_file="/app/mistral-7b-instruct-v0.1.Q4_K_M.gguf", model_type="mistral", gpu_layers=0)

    user_query = llm(request.form.get('query'))
    
    return request.form.get('query') + user_query

if __name__ == '__main__':
    app.run(debug=False)