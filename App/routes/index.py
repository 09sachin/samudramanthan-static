from .. import app
from flask import render_template,request
from ..utils.jwt import JWT
@app.route("/home")
def index():
    token=request.cookies.get("token")
    logged_in=False
    token_data=JWT.validator(token)
    if token_data:
        logged_in=True
    return render_template("index.html",logged_in=logged_in)