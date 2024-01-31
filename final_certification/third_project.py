import tkinter as tk
from tkinter import ttk
import time

def sort_sequence():
    try:
        sequence = entry.get()
        sequence_parts = [float(x.strip()) for x in sequence.split(",") if x.strip()]
        if all(isinstance(x, (int, float)) for x in sequence_parts):
            start_time = time.time()
            if sort_combobox.get() == "По возрастанию":
                sorted_sequence = sorted(sequence_parts)
            elif sort_combobox.get() == "По убыванию":
                sorted_sequence = sorted(sequence_parts, reverse=True)
            end_time = time.time()
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Отсортированная последовательность: " + ', '.join(map(str, sorted_sequence)))
            time_taken = end_time - start_time
            time_label.config(text="Время сортировки: " + "{:.6f}".format(time_taken) + " секунд")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Ошибка: Введены некорректные данные")
    except ValueError as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Ошибка: " + str(e))
    except Exception as e:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Произошла ошибка")


root = tk.Tk()
root.title("Программа сортировки")
root.geometry("400x400")

note_label = tk.Label(root, text="Введите цифры через запятую:")
note_label.pack()

entry = tk.Entry(root)
entry.pack()

sort_combobox = ttk.Combobox(root, values=["По возрастанию", "По убыванию"], state="readonly")
sort_combobox.current(0)
sort_combobox.pack()

start_button = ttk.Button(root, text="Start", command=sort_sequence)
start_button.pack()

result_label = tk.Label(root, text="Результирующий список:")
result_label.pack()

result_text = tk.Text(root, height=5, width=50, wrap="word")
result_text.pack()

time_label = tk.Label(root, text="Время сортировки: ")
time_label.pack()

root.mainloop()
