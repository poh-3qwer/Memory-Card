'''
Файл, в якому відвторено інтерфейс налаштувань
'''

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

window_menu = QWidget() # вікно головного меню
window_menu_layout = QVBoxLayout() # лейаут для вікна головного меню

questions = QListWidget()
add_question_pbtn = QPushButton("Додати питання")
remove_question_pbtn = QPushButton("Видалити питання")

question_letit = QLineEdit()
answer_ledit = QLineEdit()
wrong1_ledit =QLineEdit()
wrong2_ledit = QLineEdit()
wrong3_ledit = QLineEdit()

back_to_main_pbth = QPushButton("Повернутись в меню")

button_row_layout =QHBoxLayout()
question_form_layout = QFormLayout()

window_menu_layout.addWidget(questions)

button_row_layout.addWidget(add_question_pbtn)
button_row_layout.addWidget(remove_question_pbtn)
window_menu_layout.addLayout(button_row_layout)

question_form_layout.addRow("Введіть питання: ", question_letit)
question_form_layout.addRow("Введіть відповідь: ", answer_ledit)
question_form_layout.addRow("Введіть неправильно: ", wrong1_ledit)
question_form_layout.addRow("Введіть неправильно: ", wrong2_ledit)
question_form_layout.addRow("Введіть неправильно: ", wrong3_ledit)

window_menu_layout.addLayout(question_form_layout)

window_menu_layout.addWidget(back_to_main_pbth)

window_menu.setLayout(window_menu_layout)
