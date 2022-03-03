# 导入依赖
from flask import Flask
app = Flask(__name__)


@app.route('/hello', methods=['GET', 'POST'], endpoint='hello')
def hello():
    return "hello world"


@app.route('/hi', methods=['GET', 'POST'], endpoint='hi')
def hello():
    return "hi hi"


@app.route('/')
def index():
    return "hello world"


if __name__ == '__main__':
    app.run()
