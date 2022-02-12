from ..import app,db
from ..models.user import User
from flask import render_template,request,url_for
from ..utils.jwt import JWT
import bcrypt
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        if JWT.validator(request.cookies.get("token")):
            return url_for("index.html")
        return render_template("register.html",msg="")
    else:
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        user=User(name=name,email=email,password=bcrypt.hashpw(password.encode("ascii"),bcrypt.gensalt()),paid=False)
        db.session.add(User)
        db.session.commit()
        return render_template("register.html")