from ..import app
from flask import render_template,request,redirect,flash
from ..utils.jwt import JWT
from ..models.user import User
@app.route("/payments")
def signup():
    token=request.cookies.get("token")
    token_data=JWT.validator(token)
    if token_data:
        user=User.query.get(int(token_data["user"]))
        if user.paid:
            flash("Your payment is confirmed.")
            return redirect("events")
        return render_template("payments.html")
    flash("You need to log in first to pay.")
    return redirect('login')
