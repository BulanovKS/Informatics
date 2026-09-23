"""
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("500x250")

# функция нажатия на кнопку создает новый
# *args означает, что функция может принимать любое количество переменных.
def callback(*args):
   Label(root, text="Да!", font=('Montserrat 14 bold'), wraplength=True).pack(pady=4) #обратите внимание, что обращаемся к root как к глобальной переменной
'''
ВАЖНО!
Вы передаете функцию в виджет как объект -- поэтому она пишется здесь без скобок.
Если напишете со скобками, то она вызовется один раз и передаст как команду результат вызова (в нашем случае -- ничего).
Протестируйте это.
'''
btn = Button(root, text="Да?", command = callback)
btn.pack(ipadx=50) #ipadx задает размер кнопки по x
# делает так, чтобы при нажатии на Enter (эквивалент команды Return) тоже выполнялось callback
root.bind('<Return>', callback)
root.mainloop()
"""