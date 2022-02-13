from .. import app
from flask import redirect,url_for,make_response
@app.route("/logout")
def logout():
    resp=make_response(redirect(url_for("login")))
    resp.delete_cookie("token")
    return resp