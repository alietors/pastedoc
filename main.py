import os

from flask import Flask, render_template, request, jsonify

from db import db
from db.model.document import Document


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
    title = request.form['title']
    body = request.form['tinydata']

    doc = Document(title=title, body=body)
    db.session.add(doc)
    db.session.flush()
    db.session.commit()

    return jsonify(id=doc.id)


@app.route("/document/<int:id>", methods = ["GET"])
def get_document(id):
    document = Document.query.get(id)

    return render_template("document.html", title=document.title, body=document.body)

if __name__ == "__main__":
    app.run(debug=True)