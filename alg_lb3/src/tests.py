from alg_lb3.src.MinHeap import MinHeap


class TestCase:
    @staticmethod
    def frst_test():
        num_process = 2
        num_task = 5
        time_process = [1, 2, 3, 4, 5]
        guess_value = '0 0\n1 0\n0 1\n1 2\n0 4\n'

        answer = MinHeap(num_process, num_task, *time_process).process_time()
        assert answer == guess_value
        print('test first: OK')

    @staticmethod
    def scnd_test():
        num_process = 1
        num_task = 5
        time_process = [1, 2, 3, 4, 5]
        guess_value = '0 0\n0 1\n0 3\n0 6\n0 10\n'

        answer = MinHeap(num_process, num_task, *time_process).process_time()
        assert answer == guess_value
        print('test second: OK')

    @staticmethod
    def thrd_test():
        num_process = 12
        num_task = 5
        time_process = [1, 2, 3, 4, 5]
        guess_value = '0 0\n1 0\n2 0\n3 0\n4 0\n'

        answer = MinHeap(num_process, num_task, *time_process).process_time()
        assert answer == guess_value
        print('test third: OK')

    @staticmethod
    def four_test():
        num_process = 10
        num_task = 10
        time_process = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        guess_value = '0 0\n1 0\n2 0\n3 0\n4 0\n5 0\n6 0\n7 0\n8 0\n9 0\n'

        answer = MinHeap(num_process, num_task, *time_process).process_time()
        assert answer == guess_value
        print('test four: OK')


if __name__ == '__main__':
    case = TestCase
    case.frst_test()
    case.scnd_test()
    case.thrd_test()
    case.four_test()
