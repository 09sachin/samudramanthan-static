from ..import app
from flask import render_template,request,url_for
from ..utils.jwt import JWT
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        if JWT.validator(request.cookies.get("token")):
            return url_for("index.html")
        return render_template("register.html",msg="")
    else:
        return render_template("register.html")