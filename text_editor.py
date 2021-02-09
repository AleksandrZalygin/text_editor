import tkinter
import codecs
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile, askopenfilename, asksaveasfilename #функции "открыть как" и "сохранить как"
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

from settings import * #импортируем настройки


app=tkinter.Tk() #создание окна приложения
text=tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap='word') #создание поля с текстом

class Text_editor:
    def __init__(self):
        self.file_name=tkinter.NONE

    def new_file(self):
        self.file_name='Безымянный'
        text.delete('1.0', tkinter.END)

    def open_file(self):
        inp=askopenfile(mode="r")
        if inp is None:
            return
        with codecs.open(inp, encoding='utf-8') as f:
            data=f.read()
            text.delete('1.0', tkinter.END)
            text.insert('1.0', data)

    def save_file(self):
        data=text.get('1.0', tkinter.END)
        output=open(self.file_name, 'w', encoding='utf-8')
        output.write(data)
        output.close()

    def save_as_file(self):
        output=asksaveasfile(mode="w", defaultextension="txt")
        data=text.get('1.0', tkinter.END)
        try:
            output.write(data.rstrip())
        except Exception:
            showerror(title="Ошибка!",message="Ошибка при сохранении файла!")

    def get_info(self):
        messagebox.showinfo('Справка', "Информация о приложении")