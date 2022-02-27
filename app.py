from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, StackOverflow!</p><br> <p>Updated via VSCode</p>"


# if __name__ == '__main__':
#     app.run()


