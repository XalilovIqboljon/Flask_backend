from flask import Flask

app = Flask(__name__)
h1='''
    <h1>Assalom aleykum<h2>
    <h2>Assalom aleykum<h2>
    <h3>Assalom aleykum<h3>
    <h4>Assalom aleykum<h4>
'''

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/index')
def index():
    return "<h1>Assalom <p><h2>aleykum<h2><h1>"
@app.route('/home')
def home():
    return h1


app.run(debug=True)