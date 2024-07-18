class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)


def spin_queue(queue, n: int):
    new_array = [None for _ in range(queue.size())]
    for i in range(len(new_array)):
        new_array[int((i+n) % len(new_array))] = queue.dequeue()
    queue.queue = new_array
    return queue





