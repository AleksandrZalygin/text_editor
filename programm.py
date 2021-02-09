import tkinter
from tkinter import *
from tkinter.filedialog import askopenfile, asksaveasfile #функции "открыть как" и "сохранить как"
from tkinter.messagebox import showerror #показ всех ошибок
from tkinter import messagebox #уведомления приложения

from settings import * #импортируем настройки

from text_editor import *


#app=tkinter.Tk() #создание окна приложения
app.title(APP_NAME) #название приложения
app.minsize(width=WIDTH, height=HEIGHT)
app.maxsize(width=WIDTH, height=HEIGHT)

#text=tkinter.Text(app, width=WIDTH - 100, height=HEIGHT, wrap='word') #создание поля с текстом
scroll=Scrollbar(app, orient=VERTICAL, command=text.yview) # создание скролла
scroll.pack(side="right", fill="y") #разместили скролл
text.configure(yscrollcommand=scroll.set) #связь текста со скроллом
text.pack() #разместили поле с текстом


menuBar=tkinter.Menu(app) #создание основного меню

editor=Text_editor()

app_menu=tkinter.Menu(menuBar) #выпадающее меню "Файл"
app_menu.add_command(label="Новый файл", command=editor.new_file)
app_menu.add_command(label="Открыть файл", command=editor.open_file)
app_menu.add_command(label="Сохранить", command=editor.save_file)
app_menu.add_command(label="Сохранить как", command=editor.save_as_file)

app_menu_1=tkinter.Menu(menuBar)
app_menu_1.add_command(label="Тема")
app_menu_1.add_command(label="Шрифт")
app_menu_1.add_command(label="Цвет шрифта")

#app_menu_2=tkinter.Menu(menuBar)
#app_menu_2.add_command(label='Информация о файле')
#app_menu_2.add_command(label='Информация о папке')
#app_menu_2.add_command(label='Информация о приложении')

menuBar.add_cascade(label="Файл", menu=app_menu)
menuBar.add_cascade(label="Вид", menu=app_menu_1)
menuBar.add_cascade(label="Справка", command=editor.get_info)
menuBar.add_cascade(label="Выход", command=app.quit)

app.config(menu=menuBar) #публикуем меню

app.mainloop() # бесконечный цикл приложения