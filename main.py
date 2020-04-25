from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><p>Hello, world!</p></body></html>'

#@app.route('/name/<user>')
#def

if __name__ == '__main__':
    app.run(debug=False)