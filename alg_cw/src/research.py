from HashTable import HashTable
import random
import time
import matplotlib.pyplot as plt


def generate_random_string(str_size: int):
    result = ''
    for i in range(str_size):
        result += random.choice("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"
                                "#$%&'()*+,-./:;<=>?\@[]^_`{|}~")
    return result


def check_if_exist(list_str: list, string: str):
    for i in list_str:
        if HashTable.hash(i) is HashTable.hash(string):
            return True
    return False


def generate_uniq_string(list_size: int):
    result = []
    for i in range(list_size):
        string = generate_random_string(int(random.random() * 100) % 11 + int(random.random() * 100) % 5 + 3)
        if not check_if_exist(result, string):
            result.append(string)
        return result

def get_time_process(string_number: int, size: int):
    ht = HashTable(size)
    strings = [generate_random_string(int(random.random() * 100) % 11 + int(random.random() * 100) % 5 + 3) for _ in
               range(string_number)]
    add_times = []
    for i, string in enumerate(strings):
        time_start = time.process_time()
        ht.add(string, i + 1)
        add_times.append(time.process_time() - time_start)
    search_times = []
    for i, string in enumerate(strings):
        time_start = time.process_time()
        ht.search(string)
        search_times.append(time.process_time() - time_start)
    remove_times = []
    for i, string in enumerate(strings):
        time_start = time.process_time()
        ht.remove(string)
        remove_times.append(time.process_time() - time_start)

    return add_times, search_times, remove_times


def best_research_case():
    add_times_list = []
    search_time_list = []
    remove_times_list = []
    load_factor = 0.3
    n = 8
    size = 2**n
    number_of_iter = 10

    for _ in range(number_of_iter):
        times = get_time_process(int(size*load_factor), size)
        add_times_list.append(times[0])
        search_time_list.append(times[1])
        remove_times_list.append(times[2])
        n += 1
    return add_times_list, search_time_list, remove_times_list


def average_research_case():
    add_times_list = []
    search_time_list = []
    remove_times_list = []
    load_factor = 0.6
    n = 8
    size = 2**n
    number_of_iter = 10

    for _ in range(number_of_iter):
        times = get_time_process(int(size*load_factor), size)
        add_times_list.append(times[0])
        search_time_list.append(times[1])
        remove_times_list.append(times[2])
        n += 1
    return add_times_list, search_time_list, remove_times_list


def worst_research_case():
    add_times_list = []
    search_time_list = []
    remove_times_list = []
    load_factor = 0.9
    n = 8
    size = 2**n
    number_of_iter = 10

    for _ in range(number_of_iter):
        times = get_time_process(int(size*load_factor), size)
        add_times_list.append(times[0])
        search_time_list.append(times[1])
        remove_times_list.append(times[2])
        n += 1
    return add_times_list, search_time_list, remove_times_list


def compare_result(best_result, avrage_result, worst_result):
    best_add = best_result[0]
    best_search = best_result[1]
    best_remove = best_result[2]

    average_add = avrage_result[0]
    average_search = avrage_result[1]
    average_remove = avrage_result[2]

    worst_add = worst_result[0]
    worst_search = worst_result[1]
    worst_remove = worst_result[2]

    size_table = [2**i for i in range(8, 18)]

    #Графики иследованиий
    plt.title('Вставка')
    plt.xlabel('Размер таблицы')
    plt.ylabel('t, с')
    plt.plot(size_table, [min(elem) for elem in best_add],  '--o', label="best add")
    plt.plot(size_table, [sum(elem) / len(elem) for elem in average_add],  '--o', label="avr add")
    plt.plot(size_table, [max(elem) for elem in worst_add],  '--o', label="worst add")
    plt.legend()
    plt.show()

    plt.title('Поиск')
    plt.xlabel('Размер таблицы')
    plt.ylabel('t, с')
    plt.plot(size_table, [min(elem) for elem in best_search],  '--o', label="best search")
    plt.plot(size_table, [sum(elem) / len(elem) for elem in average_search],  '--o', label="avr search")
    plt.plot(size_table, [max(elem) for elem in worst_search],  '--o', label="worst search")
    plt.legend()
    plt.show()

    plt.title('Удаление')
    plt.xlabel('Размер таблицы')
    plt.ylabel('t, с')
    plt.plot(size_table, [min(elem) for elem in best_remove], '--o', label="best_remove")
    plt.plot(size_table, [sum(elem) / len(elem) for elem in average_remove], '--o', label="avr_remove")
    plt.plot(size_table, [max(elem) for elem in worst_remove], '--o', label="worst remove")
    plt.legend()
    plt.show()


if __name__ == '__main__':
    compare_result(best_research_case(), average_research_case(), worst_research_case())
