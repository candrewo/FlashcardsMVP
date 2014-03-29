from flask import Flask, render_template, request, session, \
    flash, redirect, url_for, g
from flask.ext.sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///flashcards.db"
app.config["SECRET_KEY"] = "Shhhh!"

db = SQLAlchemy(app)

class Question(db.Model):

    __tablename__ = "questions"

    question_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description

class Answer(db.Model):

    __tablename__ = "answers"

    answer_id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String, nullable=False)

    def __init__(self, description):
        self.description = description

    def __repr__(self):
        return self.description

@app.route('/', methods=['GET'])
def home():
    rand = random.randrange(0, db.session.query(Question).count()) 
    question = db.session.query(Question)[rand]
    # make sure answers don't repeat
    options = []
    while len(options) < 3:
        rand_answer = random.randrange(0, db.session.query(Answer).count())
        answer = db.session.query(Answer)[rand_answer]
        if answer not in options:
            options.append(answer)
    test = []
    if options[0] != options[1] and options[0] != options[2] and  options[1] != options[2]:
        test.append("")
    return render_template('home.html',question=question, options=options, test=test)


if __name__ == "__main__":
    app.run(debug=True)