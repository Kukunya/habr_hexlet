from queue import Queue
from app.cluster.task import Task
from typing import Optional


class Buffer:
    def __init__(self):
        self.queue = Queue()  # Thread-safe task queue

    def enqueue(self, task: Optional[Task]):
        """Adds a task to the queue."""
        self.queue.put(task)

    def dequeue(self, block=True) -> Optional[Task]:
        """
        Retrieves and removes a task from the queue.
        Returns None if the queue is empty or a stop signal is received.
        """
        try:
            return self.queue.get(block=block, timeout=0.1)  # Avoid indefinite blocking
        except:
            return None

    def __len__(self):
        """Returns the number of tasks in the queue."""
        return self.queue.qsize()
