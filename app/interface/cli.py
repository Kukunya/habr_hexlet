from prompt_toolkit import PromptSession
from prompt_toolkit.patch_stdout import patch_stdout
from app.cluster.buffer import Buffer
from app.cluster.cluster import Cluster
from app.cluster.task import Task


class Cli:
    def __init__(self, cluster: Cluster, buffer: Buffer):
        self.cluster = cluster  # Reference to the cluster
        self.buffer = buffer  # Reference to the shared buffer
        self.running = True
        self.session = PromptSession()  # Interactive input

    def run(self):
        """
        Main loop for handling user input and interacting with the cluster.
        """
        print("Command options: add <time>, status, exit")
        with patch_stdout():  # Ensures that print() does not interfere with input
            while self.running:
                try:
                    # Get user input
                    user_input = self.session.prompt(": ").strip()
                    self.handle_input(user_input)
                except KeyboardInterrupt:
                    print("\nPress Ctrl+D or type 'exit' to quit.")
                except EOFError:
                    print("\nExiting program.")
                    break

    def handle_input(self, user_input: str):
        """
        Processes the user input and executes the corresponding commands.
        """
        args = user_input.split()
        if not args:
            return

        cmd = args[0]
        if cmd == "exit":
            # Set running to False to exit the loop
            self.running = False
        elif cmd == "add" and len(args) > 1:
            try:
                duration = int(args[1])  # Parse task duration
                self.buffer.enqueue(Task(duration))  # Add the task to the buffer
                print(f"Task with duration {duration} added to the buffer.")
            except ValueError:
                print("Invalid duration. Please enter a valid number.")
        elif cmd == "status":
            self.cluster.display_status()
        else:
            print(f"Unknown command: {cmd}")
