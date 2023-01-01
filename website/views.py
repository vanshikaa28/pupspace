from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("timdog.html")

@views.route('/page1')
def page1():
    return render_template("front.html")
