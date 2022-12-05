import os
from flask import Flask, render_template, request, redirect



app = Flask(__name__,static_folder="static")

@app.route('/en',methods=["GET"])
def en_main_page(language = "en"):
    template_path = f"./{language}/index.html"
    return render_template(template_path)

@app.route('/vi', methods=["GET"])
def vi_main_page(language = "vi"):
    template_path = f"./{language}/index.html"
    return render_template(template_path)    


@app.route('/')
def main():
    default_path = "./en"
    return redirect(default_path)

@app.route('/result', methods=["POST"])
def process_result():
    input_essay = request.form["input_essay"]
    return input_essay