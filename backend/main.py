from flask import Flask

from flask import jsonify
from db.database import *
# print("db",db)

app = Flask(__name__)


if __name__ == '__main__':
      app.run(host="0.0.0.0",port=8000,debug=True)

@app.route("/")
def hello_world():
    all=list(Flier.select().dicts())
    print(all)
    return jsonify(all)
