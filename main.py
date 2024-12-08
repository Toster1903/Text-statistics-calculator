from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()  # создаем корневой объект - окно
root.title("Калькулятор статистики текста")  # устанавливаем заголовок окна
root.geometry("300x250")  # устанавливаем размеры окна

# Настройка строк и колонок
root.grid_rowconfigure(0, weight=1)  # Верхняя часть окна растягивается
root.grid_rowconfigure(1, weight=0)  # Нижняя строка для кнопки
root.grid_columnconfigure(0, weight=1)  # Единственная колонка растягивается

# Виджет для отображения результата
result_label = Label(root, text="Здесь будет результат", anchor="center", justify="center", wraplength=250)
result_label.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)

# Функция для открытия файла
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with open(filepath, "r") as file:
            text = file.read()
            result_label.config(text=f"Длина текста: {len(text)} символов")  # Обновляем текст в Label

# Кнопка "Открыть файл" внизу
open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky="ew", padx=10, pady=10)

root.mainloop()
