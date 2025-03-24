import sys
import heapq

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
            s += f"'{k}' весом {v};"
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

def find_path(graph, start, finish):
    """Алгоритм A*"""
    if debug:
        print("Для нахождения первого оптимального пути используем очередь с приоритетом")
        print("Приоритет = стоимость пути + эвристика")

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
                print("Полученная вершина является терминальной. Поиск окончен.")
            break

        if debug:
            print(f"Из вершины '{current}' можно попасть в:", *graph.get_to_go(current))

        for next in graph.get_to_go(current):
            new_cost = costs[current] + graph.get_cost(current, next.ch)
            if debug:
                print(f"  До вершины '{next.ch}' можно добраться за {new_cost}")

            if next.ch not in costs or new_cost < costs[next.ch]:
                priority = new_cost + heuristic(finish, next.ch)
                if debug:
                    print(f"  Добавляем '{next.ch}' в очередь с приоритетом {priority}")
                costs[next.ch] = new_cost
                heapq.heappush(q, (priority, next.ch))
                came_from[next.ch] = current

    return came_from

if __name__ == "__main__":
    start, finish = input().split()
    graph = Graph()

    while True:
        try:
            parent, child, weight = input().split()
        except (EOFError, ValueError):
            break
        if not parent or not child or not weight:
            break
        graph.add(parent, child, float(weight))

    if debug:
        print("\nВершины обработаны:")
        for key in graph.graph:
            print(f"{key}:", end=' ')
            for v in graph.graph[key]:
                print(f"{v.ch}-{v.parents[key]}", end=' ')
            print()

    res = find_path(graph, start, finish)

    if debug:
        print(f"\nПостроение пути, последняя: '{finish}'")
    res_string = back = finish
    while back != start:
        if debug:
            print(f"В вершину '{back}' пришли из '{res[back]}'")
        back = res[back]
        res_string += back

    print(res_string[::-1])
