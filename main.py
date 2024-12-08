from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from collections import Counter
import string
import matplotlib.pyplot as plt

root = Tk()  # создаем корневой объект - окно
root.title("Калькулятор статистики текста")  # устанавливаем заголовок окна
root.geometry("400x400")  # устанавливаем размеры окна

# Настройка строк и колонок
root.grid_rowconfigure(0, weight=1)  # Верхняя часть окна растягивается
root.grid_rowconfigure(1, weight=0)  # Нижняя строка для кнопок
root.grid_columnconfigure(0, weight=1)  # Единственная колонка растягивается

# Виджет для отображения результата
result_label = Label(root, text="Здесь будет результат", anchor="nw", justify="left", wraplength=350)
result_label.grid(column=0, row=0, sticky="nsew", padx=10, pady=10)

# Функция для обработки текста
def analyze_text(text):
    # Удаление пунктуации и преобразование в нижний регистр
    text_cleaned = text.translate(str.maketrans("", "", string.punctuation)).lower()
    words = text_cleaned.split()  # Разделение текста на слова
    letters = [char for char in text_cleaned if char.isalpha()]  # Список букв

    # Подсчёты
    word_count = len(words)
    char_count = len(text.replace(" ", ""))
    most_common_word = Counter(words).most_common(1)[0][0] if words else "Нет слов"
    letter_frequency = Counter(letters)

    # Формирование строки результата
    result = (
        f"Количество слов: {word_count}\n"
        f"Количество символов (без пробелов): {char_count}\n"
        f"Самое популярное слово: {most_common_word}\n"
        f"Частота букв: (График ниже)\n"
    )
    return result, letter_frequency

# Функция для построения графика
def plot_letter_frequency(letter_frequency):
    if not letter_frequency:
        return  # Если данных нет, ничего не делать

    letters, frequencies = zip(*sorted(letter_frequency.items()))
    plt.bar(letters, frequencies, color="skyblue")
    plt.title("Частота использования букв")
    plt.xlabel("Буквы")
    plt.ylabel("Частота")
    plt.show()

# Функция для открытия файла
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
            analysis_result, letter_frequency = analyze_text(text)  # Анализ текста
            result_label.config(text=analysis_result)  # Обновление текста в Label
            plot_letter_frequency(letter_frequency)  # Построение графика

# Кнопка "Открыть файл" внизу
open_button = ttk.Button(text="Открыть файл", command=open_file)
open_button.grid(column=0, row=1, sticky="ew", padx=10, pady=10)

root.mainloop()
