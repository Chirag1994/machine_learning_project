from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return "Hello Starting Machine Learning Project"


if __name__ == "__main__":
    app.run(debug=True)
