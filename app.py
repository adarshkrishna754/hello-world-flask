from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello, World!</h1>'

if __name__ == '__main__':
    # listen on all interfaces, port 5000
    app.run(host='0.0.0.0', port=5000)
