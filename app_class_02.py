from flask import Flask
app = Flask(__name__)
hello_list = ['Hello', 'World']
hello_dict = {'Hello', 'World'}

@app.route('/')
def home():
    return "Hi, I'm on the home page!"

app.run(debug=True)
