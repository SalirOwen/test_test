from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index(question:str=''):
    if question=='':
        return "<h1>我是Gemini的小助手</h1>"
    else:
       client = genai.Client()
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"{question},回答請輸出成為html格式",
    ) 
    html_format = response.text
    html_format = response.text.replace("```html","").replace("```","")
    return html_format