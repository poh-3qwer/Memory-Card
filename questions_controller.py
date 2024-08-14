from main_window import*
from random import*
from menu_window import*
#Модель питання: зберігає всю інформаціюпро нього
class Question:
    def __init__(self, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        
#клас контроллер: буде виконувати всі дії з питаннями: відбрирати рандомне і.т.д.
class QuestionController:
    def __init__(self):
        self.questions = []
        self.answer_buttons_widgets = [ans1_rbtn,ans2_rbtn, ans3_rbtn, ans4_rbtn]
        self.question_widget = question_lbl
        self.result_widget = result_lbl
        self.answers_list = questions
        self.new_question_input_question = question_letit
        self.new_question_input_answer = answer_ledit
        self.new_question_input_wrong1 = wrong1_ledit
        self.new_questions_input_wrong2 = wrong2_ledit
        self.new_questions_input_wrong3 = wrong3_ledit

    def shuffle_button(self):
        shuffle(self.answer_buttons_widgets)

    def choose_random_answer(self):
        return choice(self.questions)

    def show_questions(self):
        next_question = self.choose_random_answer()

        self.shuffle_button()

        self.question_widget.setText(next_question.question)
        self.answer_buttons_widgets[0].setText(next_question.answer)
        self.answer_buttons_widgets[1].setText(next_question.wrong_answer1)
        self.answer_buttons_widgets[2].setText(next_question.wrong_answer2)
        self.answer_buttons_widgets[3].setText(next_question.wrong_answer3)

    def add_answer(self, question):
        self.questions.append(question)
        self.answers_list.addItem(question.question)
    def remove_answer(self, id):
        pass

    def check_is_right_answer(self):
        return self.answer_buttons_widgets[0].isChecked()