from ..import app
from flask import render_template
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")