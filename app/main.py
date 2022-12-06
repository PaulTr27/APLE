import os
import requests
import json
import codecs
from flask import Flask, render_template, request, redirect, session, url_for

aple_url = 'http://paultran2734.pythonanywhere.com/'
viettelai_url = "https://viettelgroup.ai/nlp/api/v1/spell-checking"
app = Flask(__name__,static_folder="static")

@app.route('/en',methods=["GET"])
def en_main_page():
    try:
        state = json.loads(request.args['state'])
        default_text = state['result']
    except: 
        default_text = None   
    template_path = f"./en/index.html"
    is_new = False
    if default_text is None:
        is_new = True
        default_text = '''
        This is a description tab for the application\n
        Default result
        asdfklms
        adsf g/ !! 
        asdfh
        as
        '''
    default = (True if is_new else False)

    return render_template(template_path,result=default_text,default=default)

@app.route('/vi', methods=["GET"])
def vi_main_page():
    template_path = f"./vi/index.html"
    return render_template(template_path)    


@app.route('/')
def main():
    default_path = "./en"
    return redirect(default_path)

@app.route('/en', methods=["POST"])
def process_result():
    force = False
    template_path = f"./en/index.html"
    input_essay = request.form["input_essay"]
    if len(input_essay.strip()) < 10:
        state = json.dumps({"result":"Please type your essay before submitting!"})
        return redirect(url_for(".en_main_page",state=state))
    display_essay = input_essay
    payload = json.dumps({'input_text':input_essay},ensure_ascii=False)
    spell_load = {'sentence':input_essay}
    spellcheck = requests.post(url=viettelai_url,json=spell_load).json()
    if len(spellcheck) == 0 or force:
        result = requests.post(url=aple_url,json=payload)
    else:
        for i in spellcheck['result']['suggestions']:
            start = i['startIndex']
            end = i['endIndex']
            original = i['originalText']
            suggestion = i['suggestion']
            display_essay = display_essay.replace(original,
                                                  f'<span class="tooltip">{original}<span class="tooltiptext">{suggestion}</span></span>')
            
            
            
            
            

    
    return render_template(template_path,result=display_essay,default=False)