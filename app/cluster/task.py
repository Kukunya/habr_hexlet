import time


class Task:
    def __init__(self, duration: int):
        self.duration = int(duration)  # Duration of the task
        self.time_left = int(duration)  # Remaining time for the task

    def process(self):
        """Processes the task for one unit of time."""
        if self.time_left > 0:
            time.sleep(1)
            self.time_left -= 1

    def is_done(self):
        """Checks if the task is completed."""
        return self.time_left <= 0
