from flask import Flask

app=Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'

@app.route('/user/<name>')
def user_page():
    return 'User page'
if __name__=='__main__':
    app.run()