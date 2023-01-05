from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("timdog.html")

@views.route('/after_login')
def after_login():
    return render_template("front.html")

@views.route('/meet')
def meet():
    return render_template("meet.html")

@views.route('/training')
def training():
    return render_template("training.html")

@views.route('/nutrientdiet')
def nutrientdiet():
    return render_template("nutrientdiet.html")

@views.route('/page1')
def page1():
    return render_template("page1.html")

@views.route('/page2')
def page2():
    return render_template("page2.html")