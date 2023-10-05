from random import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#создание элементов интерфейса



       

app = QApplication([])

window = QWidget()

class Question():
    def __init__(self,winners,q1,q2,q3,q4):
        self.winners = winners
        self.q1 = q1
        self.q2 = q2
        self.q3 = q3
        self.q4 = q4
q1 = QRadioButton('Энцы')
q2 = QRadioButton('Смурфы')
q3 = QRadioButton('Чулымцы')
q4 = QRadioButton('Алеуты')  

RadioButton = QButtonGroup()
RadioButton.addButton(q1)
RadioButton.addButton(q2)
RadioButton.addButton(q3)
RadioButton.addButton(q4)
        
question_list = []
       
question_list.append(Question('Какой национальности не существует?','Энцы','Смурфы','Чулымцы','Алеуты'))
question_list.append(Question('Государственный язык Бразилии','Партугальский','Бразильский','Английский','Испанский'))
question_list.append(Question('Сколько будет 2 + 2 * 2','6','8','2','4'))
question_list.append(Question('Какого цвета нету на флаге России','Зелёный','Красный','Синий','Белый'))
def show_win():
    var.hide()
    result.show()
    button.setText('Следующий вопрос')
def pokaz():
    var.show()
    result.hide()
    RadioButton.setExclusive(False)
    q1.setChecked(False)
    q2.setChecked(False)
    q3.setChecked(False)
    q4.setChecked(False)
    RadioButton.setExclusive(True)


answers = [q1,q2,q3,q4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.q1)
    answers[1].setText(q.q2)
    answers[2].setText(q.q3)
    answers[3].setText(q.q4)
    winners.setText(q.winners)
    pravil.setText(q.q1)
    pokaz()
    button.setText('Ответить')
def show_correct(res):
    lb_result.setText(res)
    show_win()
def check_ans():
    print('otvet')
    if answers[0].isChecked():
        show_correct('Правильно!')
    else:
        show_correct('Неправильно!')
def next():
    current = randint(0,len(question_list)-1)
    a = question_list[current]
    ask(a)
def clickOK():
    if button.text() == 'Ответить':
        check_ans()
    else:
        next()
window.setWindowTitle('Memory Card')

window.resize(400,200)
winners = QLabel('Какой национальности не существует?')



var = QGroupBox('Варианты ответов')



button = QPushButton('Ответить')


#привязка элементов к вертикальной линии
vline2 = QHBoxLayout()
vline1 = QVBoxLayout()
vline = QVBoxLayout()

vline1.addWidget(q1)
vline1.addWidget(q2)

vline.addWidget(q3)
vline.addWidget(q4)

vline2.addLayout(vline1)
vline2.addLayout(vline)

var.setLayout(vline2)

layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout1.addWidget(winners, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout2.addWidget(var)





layout3.addStretch(1)
layout3.addWidget(button, stretch=1,alignment=Qt.AlignCenter) 
layout3.addStretch(1)



card = QVBoxLayout()


card.addLayout(layout1, stretch=2)
card.addLayout(layout2, stretch=8)
card.addStretch(1)
card.addLayout(layout3, stretch=1)
card.addStretch(1)
card.setSpacing(5) 
result = QGroupBox('Резултьтат теста')
lb_result = QLabel('Прав ты или нет?', alignment=(Qt.AlignLeft))
pravil = QLabel(q1.text(), alignment=( Qt.AlignVCenter))
Line = QHBoxLayout()
Line.addWidget(lb_result)
Line.addWidget(pravil)

result.setLayout(Line)
layout2.addWidget(result)
result.hide()
prav_otvet = QLabel('Правильный ответ')


button.clicked.connect(clickOK)
next()



window.setLayout(card)
window.show()
app.exec_()

