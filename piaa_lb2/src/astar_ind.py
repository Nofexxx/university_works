import sys
import heapq
import copy

debug = True


def heuristic(a: str, b: str):
    """Эвристическая функция расстояния между вершинами"""
    return abs(ord(a) - ord(b))


class Vertex:
    """Класс, представляющий вершину"""

    def __init__(self, ch, parent, cost):
        self.parents = {parent: cost}
        self.ch = ch

    def __str__(self):
        s = f"Вершина '{self.ch}', с ребрами от вершин: "
        for k, v in self.parents.items():
            s += f"'{k}' весом {v}; "
        return s


class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, parent: str, child: str, weight: float):
        if parent not in self.graph:
            self.graph[parent] = []
        if child not in self.graph:
            self.graph[child] = []

        self.graph[parent].append(Vertex(child, parent, weight))

        if debug:
            print(f"Добавим в граф ребро с весом {weight} между вершинами '{parent}' и '{child}'")

    def get_to_go(self, vertex):
        return self.graph[vertex]

    def get_cost(self, parent: str, child: str):
        for elem in self.graph[parent]:
            if elem.ch == child:
                return elem.parents[parent]

    def print_dict(self, d):
        for k, v in d.items():
            print(f"{k}: {v}", end=' ')
        print()


def find_path(graph: Graph, start: str, finish: str):
    print("\nПеред началом работы алгоритма отсортируем всех детей вершин по приоритету")
    for vertex in graph.graph:
        print(f"\nРассмотрим детей вершины {vertex}")
        dics = {}
        for child in graph.graph[vertex]:
            dics[child.ch] = child.parents[vertex] + heuristic(finish, child.ch)

        if dics:
            print("Неотсортированные дети и их приоритеты:")
            graph.print_dict(dics)
        else:
            print("Данная вершина детей не имеет")
            continue

        sorted_values = sorted(dics.values())
        sorted_dict = {}
        dics_copy = copy.deepcopy(dics)
        count = 0

        for i in sorted_values:
            a = min(dics_copy.items(), key=lambda x: (x[1], x[0]))
            sorted_dict[a[0]] = a[1]
            dics_copy[a[0]] = 1000  # "Удаляем" из копии
            count += 1
            print(f"Вершина {a[0]} с приоритетом {i} будет {count}-й в отсортированном списке")

        if sorted_dict:
            print("Итого отсортировано:")
            graph.print_dict(sorted_dict)

        # Перезаписываем вершины в отсортированном порядке
        graph.graph[vertex].clear()
        for i in sorted_dict.keys():
            graph.graph[vertex].append(Vertex(i, vertex, sorted_dict[i] - heuristic(finish, i)))

    print("Все вершины были отсортированы\n")

    if debug:
        print("Используем очередь с приоритетом (стоимость + эвристика)\n")

    q = []
    heapq.heappush(q, (0, start))

    came_from = {start: None}
    costs = {start: 0}

    while q:
        current = heapq.heappop(q)[1]
        if debug:
            print(f"Берём из очереди вершину '{current}'")

        if current == finish:
            if debug:
                print("Полученная вершина — конечная. Поиск завершён.")
            break

        if debug:
            print(f"Дети вершины '{current}':", *graph.get_to_go(current))

        for next_vertex in graph.get_to_go(current):
            new_cost = costs[current] + graph.get_cost(current, next_vertex.ch)

            if debug:
                print(f"  До вершины '{next_vertex.ch}' можно добраться за {new_cost}")

            if next_vertex.ch not in costs or new_cost < costs[next_vertex.ch]:
                priority = new_cost + heuristic(finish, next_vertex.ch)
                if debug:
                    print(f"  Добавим '{next_vertex.ch}' в очередь с приоритетом {priority}")
                costs[next_vertex.ch] = new_cost
                heapq.heappush(q, (priority, next_vertex.ch))
                came_from[next_vertex.ch] = current

    return came_from


if __name__ == "__main__":
    start, finish = input("Введите начальную и конечную вершины через пробел: ").split()
    graph = Graph()

    print("Введите рёбра графа (формат: from to weight), пустая строка для окончания:")

    while True:
        try:
            line = input().strip()
            if not line:
                break
            parent, child, weight = line.split()
            graph.add(parent, child, float(weight))
        except (EOFError, ValueError):
            break

    if debug:
        print("\nГраф после добавления рёбер:")
        for key in graph.graph.keys():
            print(f"{key}:", end=' ')
            for v in graph.graph[key]:
                print(f"{v.ch}-{v.parents[key]}", end=' ')
            print()

    res = find_path(graph, start, finish)

    print(f"\nПостроенный путь (обратный):")
    res_string = back = finish
    while back != start:
        if debug:
            print(f"Вершина '{back}' ← из '{res[back]}'")
        back = res[back]
        res_string += back
    print(res_string[::-1])
