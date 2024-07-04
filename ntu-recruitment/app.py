#import lib
from flask import Flask, render_template, request

#api google
import google.generativeai as palm
palm.configure(api_key="AIzaSyBF-fXqYk5VLQ6E7UIuiViLxQ-B9wScdPI")
model = {"model": "models/chat-bison-001"}

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    return(render_template("index.html"))

@app.route("/main", methods=["GET","POST"])
def main():
    return(render_template("main.html"))

@app.route("/result", methods=["GET","POST"])
def result():
    a = request.form.get("wd")
    s = request.form.get("pos")
    d = request.form.get("degree")
    f = request.form.get("age")
    g = request.form.get("sex")
    h = request.form.get("exp")
    j = request.form.get("sal")
    resultsult = a,"company is recruiting",s,"will",d,"degree with",f,"age and",g,"gender with",h,"experience and",j,"this requested salary will this person make my company better give me the answer in the HR team prospective. No more than 50 words."
    print(resultsult)
    print(a)
    resultdone = palm.chat(**model, messages=resultsult)
    return(render_template("result.html",resultdone=resultdone.last))

if __name__ == "__main__":
    app.run()
