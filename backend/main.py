from flask import Flask

app = Flask(__name__)
if __name__ == '__main__':
      app.run( port=8000)
@app.route("/")
def hello_world():
    return "<p>HACK_THE_GHOUL demo</p>"


