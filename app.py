#write me a simple hello world flask app
from flask import Flask
app = Flask(__name__)

@app.route('/myapp2')
def hello_world():
    return 'Hello World - Flask App 2'

if __name__ == '__main__':
    app.run()