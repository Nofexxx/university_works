from time import perf_counter_ns
from main import findMinPartition


def testSquares():
    printResult = False
    printDebug = False
    countSolutionsNum = False

    for i in range(2, 21):
        start = perf_counter_ns()
        findMinPartition(i, i, printResult, countSolutionsNum, printDebug)
        duration_ms = (perf_counter_ns() - start) / 1_000_000
        print(f'Размер квадрата: {i}, время работы: {duration_ms} ms.')


def testRects():
    printResult = False
    printDebug = False
    countSolutionsNum = True

    for width, height in [(12, 7), (3, 6), (5, 8), (10, 12)]:
        start = perf_counter_ns()
        print(f'Размер прямоугольника: {width}x{height}')
        findMinPartition(width, height, printResult, countSolutionsNum, printDebug)
        duration_ms = (perf_counter_ns() - start) / 1_000_000
        print(f'Время работы: {duration_ms} ms.')


# Запуск тестов
testSquares()
print('\n\n')
testRects()
