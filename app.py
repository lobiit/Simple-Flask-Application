from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/greet', methods=['POST'])
def greet():  # put application's code here
    return render_template('greet.html', name=request.form.get("name", "rav"))


if __name__ == '__main__':
    app.run()
