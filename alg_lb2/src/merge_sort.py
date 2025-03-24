from Matrix import Matrix

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if(left[i] <= right[j]):
            result.append(left[i])
            print(left[i].get_number(), end=' ')
            i += 1
        else:
            result.append(right[j])
            print(right[j].get_number(), end=' ')
            j += 1
    while i < len(left):
        result.append(left[i])
        print(left[i].get_number(), end=' ')
        i += 1
    while j < len(right):
        result.append(right[j])
        print(right[j].get_number(), end=' ')
        j += 1
    print()
    return result

def merge_sort(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = int(len(arr) / 2)
        left = merge_sort(arr[:middle])
        right = merge_sort(arr[middle:])
        return merge(left, right)

if __name__ == '__main__':
    number_matr = int(input())
    dimension_matr = int(input())
    matrixes = [Matrix()] * number_matr

    for i in range(number_matr):
        matr = []
        for j in range(dimension_matr):
            matr.append(list(map(int, input().split())))
        matrixes[i] = Matrix(matr, dimension_matr, i)
        if i + 1 < number_matr:
            dimension_matr = int(input())

    sort_value = merge_sort(matrixes)

    for elem in sort_value:
        print(elem.get_number(), end=' ')
