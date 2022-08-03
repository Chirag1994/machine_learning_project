from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def index():
    return "CI/CD Pipeline has been established."


if __name__ == "__main__":
    app.run(debug=True)
