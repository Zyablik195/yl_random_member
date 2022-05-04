from flask import Flask, render_template, request
import json
from random import randint

app = Flask(__name__)
list1 = ["/static/images/mars1.png", "/static/images/mars2.png"]

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='')

@app.route('/member')
def log():
    with open('templates/json.json', encoding='utf-8') as f:
        d = json.load(f)
        print(d)
    num = str(randint(0, len(d) - 1))
    print(num)
    args = {}
    args['title'] = ''
    args['name'] = d[num]['name']
    args['surname'] = d[num]['surname']
    args['list1'] = ', '.join(d[num]['prof'])
    args['item'] = d[num]['link']
    return render_template('login.html', **args)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')