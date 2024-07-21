class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue):
            return self.queue.pop(0)

    def size(self):
        return len(self.queue)


def spin_queue(queue, n: int):
    for _ in range(n % queue.size()):
        queue.enqueue(queue.dequeue())
    return queue





