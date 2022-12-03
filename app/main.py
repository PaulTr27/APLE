import os
from flask import Flask, render_template, request



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
    template_path = "./en/index.html"
    return render_template(template_path)