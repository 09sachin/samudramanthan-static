from .. import app
from flask import request,url_for,render_template,make_response,redirect
from ..utils.jwt import JWT
from ..models.user import User
import bcrypt
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        if JWT.validator(request.cookies.get("token")):
            return redirect(url_for("index"))
        return render_template("login.html",msg="")
    email=request.form.get("email")
    password=request.form.get("password")
    user=User.query.filter_by(email=email).first()
    if user:
        if bcrypt.checkpw(password.encode("ascii"),user.password.encode("ascii")):
            res=make_response(redirect(url_for("index")))
            token=JWT.tokenizer({"user":user.id})
            res.set_cookie("token",token,httponly=True)
            return res
    return render_template("login.html",msg="Email or password is wrong")
    