from PyQt5.QtWidgets import *
from calculator import Ui_Win1
from PyQt5.QtCore import Qt
import sys

class Window(QMainWindow,Ui_Win1):
  def __init__(self):
    super().__init__()
    self.setupUi(self)
    self.lineEdit.setAlignment(Qt.AlignRight)
    self.zero.clicked.connect(lambda: self.typing('0'))
    self.one.clicked.connect(lambda: self.typing('1'))
    self.two.clicked.connect(lambda: self.typing('2'))
    self.three.clicked.connect(lambda: self.typing('3'))
    self.four.clicked.connect(lambda: self.typing('4'))
    self.five.clicked.connect(lambda: self.typing('5'))
    self.six.clicked.connect(lambda: self.typing('6'))
    self.seven.clicked.connect(lambda: self.typing('7'))
    self.eight.clicked.connect(lambda: self.typing('8'))
    self.nine.clicked.connect(lambda: self.typing('9'))

    self.plus.setEnabled(False)
    self.minus.setEnabled(False)
    self.mod.setEnabled(False)
    self.divide.setEnabled(False)
    self.multiply.setEnabled(False)
    self.breacketleft.setEnabled(False)
    self.bracketright.setEnabled(False)
    self.point.setEnabled(False)
    self.delete.setEnabled(False)
    self.clear.setEnabled(False)
    self.equal.setEnabled(False)
    
    self.plus.clicked.connect(lambda: self.things('+'))
    self.minus.clicked.connect(lambda: self.things('-'))
    self.mod.clicked.connect(lambda: self.things('%'))
    self.divide.clicked.connect(lambda: self.things('/'))
    self.multiply.clicked.connect(lambda: self.things('*'))
    self.breacketleft.clicked.connect(lambda: self.breacket(')'))
    self.bracketright.clicked.connect(lambda: self.breacket('('))
    self.point.clicked.connect(lambda: self.things('.'))
    self.delete.clicked.connect(lambda: self.dell(2))
    self.clear.clicked.connect(lambda: self.dell(1))
    self.equal.clicked.connect(self.score)

  def dell(self,o):
    if o == 1:
      self.lineEdit.setText(' ')
    else:
     self.lineEdit.setText(self.lineEdit.text()[:-1])
  
  def things(self,ty):
    t = self.lineEdit.text()
    if  t[-1] != '+'  and  t[-1] != '-' and t[-1] != '/' and t[-1] != '*' and t[-1] != '%':
      self.lineEdit.setText(t+ty)
   
  def breacket(self,ty):
    t = self.lineEdit.text()
    if ty == '(' and (t[-1] == '+'  or  t[-1] == '-' or t[-1] == '/' or t[-1] == '*' or t[-1] == '%'):
      self.lineEdit.setText(t+ty)
    elif t[-1] != '+'  and  t[-1] != '-' and t[-1] != '/' and t[-1] != '*' and t[-1] != '%':
      self.lineEdit.setText(t+ty)

  def typing(self,ty):
    self.plus.setEnabled(True)
    self.minus.setEnabled(True)
    self.mod.setEnabled(True)
    self.divide.setEnabled(True)
    self.multiply.setEnabled(True)
    self.breacketleft.setEnabled(True)
    self.bracketright.setEnabled(True)
    self.point.setEnabled(True)
    self.delete.setEnabled(True)
    self.clear.setEnabled(True)
    self.equal.setEnabled(True)

    t = self.lineEdit.text()
    self.lineEdit.setText(t+ty)
  
  def score(self):
    t = self.lineEdit.text()
    if len(t)>1 and t[-1] == '0' and t[-2] == '/' :
      self.lineEdit.setText('Can\'t divide by zero!')
    else:
      s = eval(self.lineEdit.text())
      self.lineEdit.setText(f'{s}')
    
    

if __name__ == "__main__":
  app = QApplication(sys.argv)
  window = Window()
  window.show()
  app.exec_()