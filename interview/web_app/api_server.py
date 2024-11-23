"""
Main back-end Controller
"""

import os

from flask import Flask, jsonify, request, Response, render_template, redirect, url_for
from sqlalchemy import create_engine, asc, func, delete
from sqlalchemy.orm import sessionmaker
from models.db_setup import Base, Questions


__version__     = '0.0.1'
__status__      = 'Prototype'
__author__      = 'Brindal Patel'
__maintainer__  = 'Brindal Patel'


curr_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(*[os.path.dirname(os.path.abspath(__file__)), \
                                                    "views", "templates"])
static_dir = os.path.join(*[os.path.dirname(os.path.abspath(__file__)), \
                                                    "views", "static"])
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)


# Connect to Database and create database session
db_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "quesions.db")
db_uri = 'sqlite:///{}'.format(db_dir)
engine = create_engine(db_uri, \
                        connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/', methods=['GET'])
def welcome_page():
    """Home page"""
    return render_template('home.html')


@app.route('/solved', methods=['GET'])
def solved_questions_list():
    questions = session.query(Questions).filter_by(solved=True).order_by(asc(Questions.id)).all()
    count = count_solved_questions()
    return render_template('questions.html', questions=questions, count=count, button=None)


@app.route('/all', methods=['GET'])
def all_questions_list():
    questions_list = session.query(Questions).order_by(asc(Questions.id)).all()
    count = count_solved_questions()
    return render_template('questions.html', questions=questions_list, count=count, button=None)


@app.route('/pick_one', methods=['GET'])
def pick_a_question():
    question = session.query(Questions).filter_by(solved=False).order_by(func.random()).first()

    if question is None:
        button = None
        q = None
    else:
        button = 1
        q = [question]
    return render_template('questions.html', questions=q, button=button)


@app.route('/reset_status', methods=['GET'])
def reset_status():
    question = session.query(Questions).filter_by(solved=True).update(dict(solved=False))
    session.commit()
    return redirect(url_for('welcome_page'))


@app.route('/<int:question_id>/update_status', methods=['GET'])
def change_status(question_id):
    question = session.query(Questions).filter_by(id=question_id).first()
    question.solved = True
    session.commit()
    return redirect(url_for('welcome_page'))

"""
@app.route('/<int:question_id>/update_question', methods=['GET'])
# TODO: add front-end view and update method to have get and post
def change_question_info(question_id):
    question = session.query(Questions).filter_by(id=question_id).first()
    q = {
        "name": "Empty",
        "descriptions": "",
        "example": "",
        "reference": "",
    }
    question.name = q["name"]
    question.descriptions=q["descriptions"]
    question.example=q["example"]
    question.reference=q["reference"]
    session.commit()
    return redirect(url_for('welcome_page'))

@app.route('/<int:question_id>/delete_question', methods=['GET'])
# TODO: add front-end view and update method to have get and post
def delete_question_info(question_id):
    question = session.query(Questions).filter_by(id=question_id).first()
    session.delete(question)
    session.commit()
    return redirect(url_for('welcome_page'))
"""

def count_solved_questions():
    count_all = session.query(Questions).count()
    count_solved = session.query(Questions).filter_by(solved=True).count()
    question_count = str(count_solved) + "/" + str(count_all)
    return question_count


if __name__ == '__main__':
    app.secret_key = 'super_batman_secret_key'
    app.debug = True
    app.run(threaded=True, host = '0.0.0.0', port =5000)
