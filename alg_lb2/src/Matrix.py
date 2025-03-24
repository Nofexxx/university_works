class Matrix:
    def __init__(self, lst_matr=None, dimension=None, number=None):
        self.matr = lst_matr
        self.dimension = dimension
        self.number = number

    def __len__(self):
        return self.dimension

    def __eq__(self, other):
        return self.get_trace_sum() == other.get_trace_sum()

    def __gt__(self, other):
        return self.get_trace_sum() > other.get_trace_sum()

    def __ge__(self, other):
        return self.get_trace_sum() >= other.get_trace_sum()

    def __lt__(self, other):
        return self.get_trace_sum() < other.get_trace_sum()

    def __le__(self, other):
        return self.get_trace_sum() <= other.get_trace_sum()

    def print_matrix(self):
        for i in range(self.dimension):
            for j in range(self.dimension):
                print(self.matr[i][j], end=' ')
            print()
        print(self.get_trace_sum())

    def get_number(self):
        return self.number

    def get_trace_sum(self):
        sum = 0
        for i in range(self.dimension):
            sum += self.matr[i][i]
        return sum