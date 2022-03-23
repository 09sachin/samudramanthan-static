from ..import app,db
from ..models.user import User
from flask import render_template,request,url_for,redirect
from ..utils.jwt import JWT
import bcrypt
@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        if JWT.validator(request.cookies.get("token")):
            return url_for("index")
        return render_template("register.html",msg="")
    else:
        name=request.form["name"]
        email=request.form["email"]
        password=request.form["password"]
        if len(User.query.filter_by(email=email).all()) >0:
            return render_template("register.html",msg="This email already exists.")
        user=User(name=name,email=email,password=bcrypt.hashpw(password.encode("ascii"),bcrypt.gensalt()),paid=False)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))