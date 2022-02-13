from .. import app
from flask import render_template
@app.route("/sponsors")
def sponsor():
    return render_template("sponsors.html")