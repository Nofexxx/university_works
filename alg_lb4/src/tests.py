from alg_lb4.src.Alghoritm import RabinKarpAlghoritm

class TestCases:
    @staticmethod
    def frst_test():
        answer = RabinKarpAlghoritm().matcher('aba', 'abacaba')
        guess_value = [0, 4]
        assert answer == guess_value
        print('test first: ok')

    @staticmethod
    def scnd_test():
        answer = RabinKarpAlghoritm().matcher('aaaaa', 'aaaaaaaaaaaa')
        guess_value = [0, 1, 2, 3, 4, 5, 6, 7]
        assert answer == guess_value
        print('test second: ok')

    @staticmethod
    def thrd_test():
        answer = RabinKarpAlghoritm().matcher('aba', 'qwertyuiopmnbbvccxz')
        guess_value = []
        assert answer == guess_value
        print('test third: ok')

    @staticmethod
    def four_test():
        answer = RabinKarpAlghoritm().matcher('Hello', 'Hello my friend. Do you know how print Hellow wolrd on c++')
        guess_value = [0, 39]
        assert answer == guess_value
        print('test four: ok')

if __name__ == '__main__':
    case = TestCases
    case.frst_test()
    case.scnd_test()
    case.thrd_test()
    case.four_test()
