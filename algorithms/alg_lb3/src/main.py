from MinHeap import MinHeap

if __name__ == '__main__':
    num_process, num_task = map(int, input().split())
    times = list(map(int, input().split()))
    heap = MinHeap(num_process, num_task, *times)
    result = heap.process_time()
    print(result)
