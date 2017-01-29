import os

from flask import Flask, render_template, redirect, request

from db import db
from db.model.note import Note


def create_app():
    app = Flask(__name__)
    basedir = os.path.abspath(os.path.dirname(__file__))
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
    db.init_app(app)
    return app

app = create_app()
db.create_all(app=app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/document", methods = ["POST"])
def create_document():
    title = "My Document"
    body = request.form["tinydata"]

    note = Note(title=title, body=body)
    db.session.add(note)
    db.session.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)