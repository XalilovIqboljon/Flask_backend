from flask import Flask

app = Flask(__name__)
h1='''
    <h1>Assalom aleykum<h2>
    <h2>Assalom aleykum<h2>
    <h3>Assalom aleykum<h3>
    <h4>Assalom aleykum<h4>
'''
commen='''
    <table border="1">
        <tr>
            <td>Ism</td>
            <td>Familiya</td>
            <td>Otasini ismi</td>
        </tr>
        <tr>
            <td>Iqboljon</td>
            <td>Xalilov</td>
            <td>Qodirjon o'g'li</td>
        </tr>
'''

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/comment')
def comm():
    return commen

@app.route('/index')
def index():
    return "<h1>Assalom <p><h2>aleykum<h2><h1>"

@app.route('/home')
def home():
    return h1


app.run(debug=True)