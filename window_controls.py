from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from main_window import*
from menu_window import*

from questions_controller import*

q1 = Question(question = " 5 + 5", answer="10", wrong_answer1="9", wrong_answer2="15", wrong_answer3="25")
q2 = Question(question = "Коли зробили Among Us?", answer="2018", wrong_answer1="2002", wrong_answer2="2013", wrong_answer3="2021")

question_controller = QuestionController()
question_controller.add_answer(q1)
question_controller.add_answer(q2)
def show_question():
    result_gbox.hide()
    answers_gbox.show()
    question_controller.show_questions()

def show_results():
    result_gbox.show()
    answers_gbox.hide()

def check_manager():
    if give_answer_pbtn.text() == "Відповісти":
        show_results()
        give_answer_pbtn.setText("Наступне питання")

    elif give_answer_pbtn.text() == "Наступне питання":
        show_question()
        give_answer_pbtn.setText("Відповісти")

def show_menu():
    window_menu.show()
    window_main.hide()

def show_main():
    window_main.show()
    window_menu.hide()

def connect_button():
    menu_pbtn.clicked.connect(show_menu)
    give_answer_pbtn.clicked.connect(check_manager)
    back_to_main_pbth.clicked.connect(show_main)