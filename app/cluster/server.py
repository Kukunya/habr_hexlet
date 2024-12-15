import threading
import time
from typing import Optional
from app.cluster.task import Task
from app.cluster.buffer import Buffer


class Server(threading.Thread):
    def __init__(self, id: int, buffer: Buffer):
        super().__init__()
        self.id = id  # Server ID
        self.buffer = buffer  # Shared task buffer
        self.current_task: Optional[Task] = None  # Currently assigned task
        self.running = True  # Server status flag

    def assign_task(self, task: Task):
        """Assigns a task to the server."""
        self.current_task = task

    def run(self):
        """Main server loop to process tasks."""
        while self.running:
            if self.current_task:
                # Process the current task
                self.current_task.process()
                if self.current_task.is_done():
                    print(f"Server {self.id} completes execution.")
                    self.current_task = None  # Task is completed
            else:
                # If idle, fetch a new task from the buffer
                task = self.buffer.dequeue(block=False)
                if task is None:
                    time.sleep(0.1)  # Short sleep to avoid tight looping
                    continue
                self.assign_task(task)
                print(f"The task from the queue is sent to Server {self.id}.")

    def stop(self):
        """Stops the server."""
        self.running = False
        self.buffer.enqueue(None)  # Signal the server to stop

    def get_status(self):
        """Returns the status of the server."""
        if self.current_task:
            return f"Server {self.id}: Task ({self.current_task.time_left} sec left)"
        return f"Server {self.id}: idle"
