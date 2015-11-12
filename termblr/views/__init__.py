# from .app import route
# from flask.ext.admin import expose
import flask
from flask import url_for, send_file, render_template, send_from_directory


simpleview = flask.Blueprint(
    'simpleview',
    __name__,
    template_folder='templates',
    static_folder='static'
)


@simpleview.route('/base', methods=['GET'])
def base():
    return render_template("base.html")


@simpleview.route('/', methods=['GET'])
def main():
    return render_template("index.html")
