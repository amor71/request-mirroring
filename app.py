from flask import Flask

app = Flask(__name__)

@app.route('/endpoint')
def endpoint():
    return 'Response from Flask Server'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

