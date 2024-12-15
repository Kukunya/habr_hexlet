from app.cluster.buffer import Buffer
from app.cluster.server import Server


class Cluster:
    def __init__(self, buffer: Buffer, server_count: int):
        self.buffer = buffer  # Shared task buffer
        self.servers = [Server(i + 1, buffer) for i in range(server_count)]  # List of server threads

    def start(self):
        """Starts all servers."""
        for server in self.servers:
            server.start()

    def stop(self):
        """Stops all servers."""
        for server in self.servers:
            server.stop()
        for server in self.servers:
            server.join()  # Waits for the thread to finish

    def display_status(self):
        """Displays the status of all servers and the task queue."""
        for server in self.servers:
            print(server.get_status())  # Fetch the status from each server
        print(f"Queue: {len(self.buffer)} tasks")
