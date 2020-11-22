from flask import Flask


def create_app() -> Flask:
    app = Flask(__name__)

    @app.route("/hello/text")
    def hello_text() -> str:
        return "Hello, World!"

    @app.route("/hello/json")
    def hello_json() -> dict:
        return {"text": "Hello, World!"}

    return app