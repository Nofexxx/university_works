class MinHeap:
    def __init__(self, num_process, num_task, *times):
        self.number_process = num_process
        self.task = num_task
        self.times = [i for i in range(num_task)]

        self.processors = [[i, 0] for i in range(num_process)]
        for i in range(num_task):
            self.times[i] = times[i]

    def sift_down(self, index):
        max_index = index
        left_child = self.left_child(index)
        if left_child > 0:
            if self.processors[left_child][1] < self.processors[max_index][1]:
                max_index = left_child
            if self.processors[left_child][1] == self.processors[max_index][1]:
                if self.processors[left_child][0] < self.processors[max_index][0]:
                    max_index = left_child

        right_child = self.right_child(index)
        if right_child > 0:
            if self.processors[right_child][1] < self.processors[max_index][1]:
                max_index = right_child
            if self.processors[right_child][1] == self.processors[max_index][1]:
                if self.processors[right_child][0] < self.processors[max_index][0]:
                    max_index = right_child

        if index != max_index:
            self.processors[index], self.processors[max_index] = self.processors[max_index], self.processors[index]
            self.sift_down(max_index)

    def process_time(self):
        answer = ''
        for i in range(self.task):
            answer += str(self.processors[0][0]) + ' ' + str(self.processors[0][1]) + '\n'
            self.processors[0][1] += self.times[i]
            self.sift_down(0)
        return answer

    @staticmethod
    def parent(index):
        if (index - 1)//2 < 0:
            return 0
        return (index - 1) // 2

    def left_child(self, index):
        if (2 * index + 1) < self.number_process:
            return 2 * index + 1
        return -1

    def right_child(self, index):
        if (2 * index + 2) < self.number_process:
            return 2 * index + 2
        return - 1
