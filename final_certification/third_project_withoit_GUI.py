import time

def sort_sequence(sequence, order):
    try:
        sequence_parts = [float(x.strip()) for x in sequence.split(",") if x.strip()]
        start_time = time.time()
        if order == "ascending":
            sorted_sequence = sorted(sequence_parts)
        elif order == "descending":
            sorted_sequence = sorted(sequence_parts, reverse=True)
        end_time = time.time()
        time_taken = end_time - start_time
        return sorted_sequence, time_taken
    except ValueError as e:
        return "Ошибка: " + str(e), -1
    except Exception as e:
        return "Произошла ошибка", -1


if __name__ == '__main__':
    input_sequence = input("Введите последовательность чисел через запятую: ")
    sort_order = input("Выберите порядок сортировки (ascending/descending): ")

    sorted_result, time_taken = sort_sequence(input_sequence, sort_order)
    if time_taken != -1:
        print("Отсортированная последовательность:", sorted_result)
        print("Время сортировки: {:.6f} секунд".format(time_taken))
    else:
        print("Ошибка при сортировке:", sorted_result)
