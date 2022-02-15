from .. import app
from flask import redirect, render_template,request, url_for
from ..utils.jwt import JWT
@app.route("/")
def home():
    return redirect(url_for('index'))
@app.route("/home")
def index():
    token=request.cookies.get("token")
    logged_in=False
    token_data=JWT.validator(token)
    if token_data:
        logged_in=True
    return render_template("index.html",logged_in=logged_in)