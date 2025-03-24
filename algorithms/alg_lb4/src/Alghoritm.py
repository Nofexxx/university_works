class RabinKarpAlghoritm:
    @staticmethod
    def hashing(string):
        return sum(ord(cymb) for cymb in string)

    def matcher(self, pattern, string):
        h, len_pat = self.hashing(pattern), len(pattern)
        sub_h = self.hashing(string[:len_pat])
        indexes = [0] if h == sub_h and string[:len_pat] == pattern else []
        for i in range(1, len(string) - len_pat + 1):
            sub_h = sub_h - ord(string[i-1]) + ord(string[i+len_pat-1])
            if h == sub_h and string[i:i+len_pat] == pattern:
                indexes.append(i)
        return indexes


class Inerface:
    def __init__(self):
        self.alghoritm = RabinKarpAlghoritm

    @staticmethod
    def run():
        pattern, string = input(), input()
        answer = RabinKarpAlghoritm().matcher(pattern, string)
        print(*answer)