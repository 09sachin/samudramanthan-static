from ..import app
from flask import render_template
@app.route("/teams")
def team():
    return render_template("team.html")