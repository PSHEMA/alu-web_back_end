#!/usr/bin/env python3
""" Basic Flask App """
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """ class Config """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ get_locale """
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def index():
    """ index """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
