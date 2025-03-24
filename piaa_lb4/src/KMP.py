def prefix_func(s):
    prefix = [0] * len(s)
    for i in range(1, len(s)):
        if debug:
            print(f'Префикс-функция для подстроки {s[0:i+1]}')
        k = prefix[i - 1]
        if debug:
            print(f'Рассмотрим префикс: {s[0:k+1]}')
        while k > 0 and s[k] != s[i]:
            k = prefix[k - 1]
            if debug:
                print(f'Рассмотрим предыдущий префикс-суффикс: {s[0:k+1]}')
        if s[k] == s[i]:
            k += 1
            if debug:
                print('Это префикс-суффикс')
        prefix[i] = k
        if debug:
            print(f'Для подстроки {s[0:i+1]} префикс-функция: {k}\n')
    return prefix


def find_cyclic_shift(p, t):
    len_1, len_2 = len(p), len(t)
    if len_1 != len_2:
        print(-1)
        return

    prefix = prefix_func(p)
    if debug:
        print(f'Префикс-функция: {prefix}')

    t *= 2
    prev_prefix = int(t[0] == p[0])
    for i in range(1, len(t)):
        cur_prefix = prev_prefix
        if debug:
            print(f'Префикс функция для {t[0:len_1+i - 2]}')
        while cur_prefix > 0 and p[cur_prefix] != t[i]:
            cur_prefix = prefix[cur_prefix - 1]
            if debug:
                print(f'Рассмотрим предыдущий префикс-суффикс: {t[0:cur_prefix+1]}')
        if p[cur_prefix] == t[i]:
            cur_prefix += 1
            if debug:
                print(f'Найдено расширение префикс-суффикса {t[0:cur_prefix]}')
        if debug:
            print(f'Для подстроки {t[0:len_1 + i - 2]}: префикс-функция: {cur_prefix}\n')
        if cur_prefix == len_1:
            print((i + 1) - len_1)
            return
        prev_prefix = cur_prefix
    print(-1)


def find_occurrences(p, t):
    prefix = prefix_func(p + '%' + t)
    if debug:
        print(f'Префикс-функция: {prefix}')

    nums = []
    len_substr = len(p)
    if debug:
        print(f'Ищем значение префикс-функции, равное {len_substr}')
    for ind in range(len(t)):
        if debug:
            print(f'\nРассмотрим индекс {ind}')
        if prefix[len_substr + ind + 1] == len_substr:
            if debug:
                print(f'Значение префикс-функции: {len_substr} - найдено вхождение в индексе {ind - len_substr + 1}')
            nums.append(ind - len_substr + 1)
        elif debug:
            print(f'Значение префикс-функции: {prefix[len_substr + ind + 1]}')

    if nums:
        print(*nums, sep=',')
    else:
        print(-1)


if __name__ == '__main__':
    debug = True
    step = 1
    p = input()
    t = input()
    if step == 1:
        find_occurrences(p, t)
    else:
        find_cyclic_shift(p, t)