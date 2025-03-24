from HashTable import HashTable
from research import generate_uniq_string


class MyTestCase:
    def test_hash_table(self):
        ht = HashTable(997)
        strings = generate_uniq_string(1000000)
        iter_number = 10

        for _ in range(iter_number):
            for i, string in enumerate(strings):
                assert ht.add(string, i + 1) is True
            print('test add: OK')
            for i, string in enumerate(strings):
                assert ht.search(string) is True
            print('test search: OK')
            for i, string in enumerate(strings):
                assert ht.remove(string) is True
            print('test remove: OK')
        print('all tests passed')


if __name__ == '__main__':
    case = MyTestCase()
    case.test_hash_table()
