from merge_sort import Matrix, merge_sort

class TestCauses:

    @staticmethod
    def frst_test():
        matr1 = [[-62, -8], [-1, 97]]
        matr2 = [[-98, -84, 28], [32, -85, -33], [96, -68, -99]]
        matr3 = [[15, 81], [67, 68]]
        check = []
        gues_value = [1, 0, 2]

        matixes = [Matrix(matr1, 2, 0), Matrix(matr2, 3, 1), Matrix(matr3, 2, 2)]
        sort = merge_sort(matixes)
        for item in sort:
            check.append(item.get_number())
        assert check == gues_value
        print('first test: OK')

    @staticmethod
    def scnd_test():
        matr = [[-92, 77, -12], [73, 81, 100], [-11, 44, -55]]
        check = []
        gues_value = [0]

        matrix = [Matrix(matr, 3, 0)]
        sort = merge_sort(matrix)
        for item in sort:
            check.append(item.get_number())
        assert check == gues_value
        print('second test: OK')

    @staticmethod
    def thrd_test():
        matr1 = [[1, 0], [0, 1]]
        matr2 = [[1, 77], [-12, 1]]
        matr3 = [[1, -4], [22, 1]]

        check = []
        gues_value = [0, 1, 2]

        matrixes = [Matrix(matr1, 2, 0), Matrix(matr2, 2, 1), Matrix(matr3, 2, 2)]
        sort = merge_sort(matrixes)
        for item in sort:
            check.append(item.get_number())
        assert check == gues_value
        print('third test: OK')

if __name__ == '__main__':
    case = TestCauses
    case.frst_test()
    case.scnd_test()
    case.thrd_test()
