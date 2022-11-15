from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/greet')
def greet():  # put application's code here
    return render_template('greet.html', name=request.args.get("name", "rav"))


if __name__ == '__main__':
    app.run()
