from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/form")
def form():
    return render_template("form.html")
@app.route("/post", methods =["POST"])
def post():
    name=request.form.get("name")
    pname=request.form.get("pname")
    lastname=request.form.get("lastname")
    age=request.form.get("age")
    return render_template("post.html", name =name,lastname=lastname,pname=pname,age=age)
@app.route("/blog")
def blog():
    return render_template("blog.html")

