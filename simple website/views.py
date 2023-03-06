from flask import Blueprint, render_template, jsonify, request, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/")
def home():
    return render_template("index.html", name="shashank")

@views.route("/profile/<username>")
def profile(username):
    return render_template("index.html", name=username)

@views.route("/json")
def get_json():
    return jsonify({'name': 'tim', 'coolness': 10})

@views.route("/data")
def get_data():
    data = request.json
    return jsonify(data)

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.get_json"))