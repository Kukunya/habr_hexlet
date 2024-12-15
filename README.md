
# **Distributed System Simulator**

This is a Python-based distributed system simulator. It models a system with multiple servers that process tasks distributed through a shared task buffer. The simulation is interactive, allowing users to add tasks, monitor server status, and exit the program gracefully.

---

## **Features**

- Interactive command-line interface (CLI).
- Support for multiple servers working concurrently.
- Tasks with custom durations.
- Thread-safe task queue (`Buffer`) for distributing tasks.
- Graceful shutdown with proper cleanup of resources.
- Real-time server status updates.

---

## **Technologies Used**

- **Python 3.x**: Programming language.
- **Threading**: For concurrent server simulation.
- **Prompt Toolkit**: For interactive and user-friendly CLI.
- **Queue**: For thread-safe task management.

---

## **Installation**

1. Clone the repository or download the code:
   ```bash
   git clone https://github.com/Kukunya/habr_hexlet_cluster_imitation.git
   cd habr_hexlet_cluster_imitation
   ```

2. Install required dependencies:
   ```bash
   pip install prompt_toolkit
   ```

3. Run the program:
   ```bash
   python main.py
   ```

---

## **Usage**

1. Start the program and specify the number of servers:
   ```plaintext
   Specify the number of servers: 3
   ```

2. Use the following commands in the interactive prompt:

   - **`add <time>`**
     - Adds a task with the specified duration (in seconds) to the task buffer.
     - Example:
       ```plaintext
       : add 5
       Task with duration 5 added to the buffer.
       ```

   - **`status`**
     - Displays the current status of all servers and the task queue.
     - Example:
       ```plaintext
       : status
       Server 1: Task (4 sec left)
       Server 2: idle
       Queue: 0 tasks
       ```

   - **`exit`**
     - Gracefully shuts down the servers and exits the program.
     - Example:
       ```plaintext
       : exit
       Exiting program.
       ```

---

## **Example Session**

```plaintext
Specify the number of servers: 2
Command options: add <time>, status, exit
: add 5
Task with duration 5 added to the buffer.
The task from the queue is sent to Server 1.
: add 3
Task with duration 3 added to the buffer.
The task from the queue is sent to Server 2.
: status
Server 1: Task (4 sec left)
Server 2: Task (2 sec left)
Queue: 0 tasks
: add 7
Task with duration 7 added to the buffer.
: status
Server 1: Task (3 sec left)
Server 2: Task (1 sec left)
Queue: 1 tasks
Server 2 completes execution.
The task from the queue is sent to Server 2.
: exit
Exiting program.
```

---

## **Project Structure**

- **`main.py`**: Entry point of the program.
- **`app/`**: Contains the main modules:
  - **`cluster/`**
    - **`buffer.py`**: Implements a thread-safe task queue.
    - **`cluster.py`**: Manages servers and handles task distribution.
    - **`server.py`**: Simulates a server that processes tasks.
    - **`task.py`**: Represents a task with a duration.
  - **`interface/`**
    - **`cli.py`**: Provides the interactive command-line interface.

---

## **How It Works**

1. **Initialization**:
   - The user specifies the number of servers at the start.
   - Servers and the shared task buffer are initialized.

2. **Task Addition**:
   - Users can add tasks with the `add <time>` command.
   - Tasks are placed in the `Buffer` and distributed to idle servers.

3. **Task Execution**:
   - Servers process tasks in real-time, decrementing the task's remaining time.
   - When a task is completed, the server fetches the next task from the buffer.

4. **Status Updates**:
   - The `status` command shows:
     - Current tasks assigned to servers.
     - Remaining time for each task.
     - Number of tasks in the buffer.

5. **Graceful Shutdown**:
   - The `exit` command stops all servers and ends the program.

---

## **Key Design Principles**

- **Thread Safety**: The `Buffer` uses a thread-safe queue to avoid race conditions.
- **Concurrency**: Servers run in separate threads, simulating real distributed processing.
- **User Experience**: The CLI uses `prompt_toolkit` for a smooth, interactive experience.

---

## **Contributing**

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push the branch.
4. Submit a pull request.

---

## **License**

This project is licensed under the MIT License.

---
