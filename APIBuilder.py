# import libraries
from flask import Flask, jsonify, request

app = Flask(__name__)


# 路由与视图函数
@app.route('/hello', methods=['GET', 'POST'], endpoint='hello')
def hello():
    return '<h1>Hello World!</h1>'


# 动态路由
@app.route('/user/<string:name>', methods=['GET'])
def user(name):
    return '<h1>%s, Hello World!</h1>' % name


# Test: GET method
@app.route('/', methods=['GET'])
def check():
    return jsonify({'message': 'It works'})


# Data
data = [{'id': 1, 'name': 'iishi', 'subject': 'math'},
        {'id': 2, 'name': 'eesha', 'subject': 'science'},
        {'id': 3, 'name': 'aryan', 'subject': 'english'},
        {'id': 4, 'name': 'jack', 'subject': 'math'}]


# GET method for data
@app.route('/class_info', methods=['GET'])
def classroom_info():
    return jsonify({'classroom': data})


# GET method for specific data
@app.route('/subject/<string:subj>', methods=['GET'])
def subject_info(subj):
    student_info = [info for info in data if info['subject'] == subj]
    return jsonify({subj: student_info})


# POST method
@app.route('/class_info', methods=['POST'])
def new_data():
    new = {
        'id': request.json['id'],
        'name': request.json['name'],
        'subject': request.json['subject']
    }
    data.append(new)
    return jsonify({'classroom': data})


# PUT method
@app.route('/subject_change/<string:name>', methods=['PUT'])
def subj_change(name):
    student_info = [info for info in data if info['name'] == name]
    student_info[0]['subject'] = request.json['subject']
    return jsonify({'student': student_info[0]})


# DELETE Method
@app.route('/delete/<string:name>', methods=['delete'])
def delete(name):
    student_info = [info for info in data if info['name'] == name]
    data.remove(student_info[0])
    return jsonify({'classroom': data})


if __name__ == '__main__':
    app.run(debug=True)
