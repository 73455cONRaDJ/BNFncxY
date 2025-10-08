# 代码生成时间: 2025-10-08 19:42:51
import numpy as np
import psutil
import os
import signal

"""
A simple process manager module using Python and NumPy for managing system processes.
It allows listing, killing, and monitoring system processes.
"""


# Define a class for process management
class ProcessManager:
    def __init__(self):
        """Initialize the process manager."""
        self.process_list = []

    def list_processes(self):
        """
        List all processes currently running on the system.
        Returns a list of tuples, each containing the process ID and name.
        """
        try:
            self.process_list = [(proc.pid, proc.name()) for proc in psutil.process_iter()]
            return self.process_list
        except Exception as e:
            print(f"Error listing processes: {e}")
            return []

    def kill_process(self, pid):
        """
        Kill a process by its ID.
        Raises an exception if the process does not exist or cannot be killed.
        """
        try:
            process = psutil.Process(pid)
            process.terminate()
            process.wait()
            print(f"Process {pid} terminated.")
        except psutil.NoSuchProcess:
            print(f"No process found with ID {pid}.")
        except psutil.AccessDenied:
            print(f"Access denied to terminate process {pid}.")
        except Exception as e:
            print(f"Error terminating process {pid}: {e}")

    def monitor_memory_usage(self, interval=1):
        """
        Monitor the memory usage of all processes at a specified interval (in seconds).
        Prints the process ID, name, and memory usage percentage.
        """
        print("Monitoring memory usage...")
        try:
            while True:
                for proc in psutil.process_iter():
                    try:
                        mem_info = proc.memory_info()
                        pid = proc.pid
                        print(f"PID: {pid}, Name: {proc.name()}, Memory Usage: {mem_info.rss / (1024 * 1024)} MB")
                    except (psutil.NoSuchProcess, psutil.AccessDenied):
                        continue
                np.pause(interval)  # Use NumPy's pause function to wait
        except KeyboardInterrupt:
            print("Monitoring stopped by user.")

# Example usage of the ProcessManager class
if __name__ == '__main__':
    manager = ProcessManager()
    processes = manager.list_processes()
    print("Current running processes:")
    for pid, name in processes:
        print(f"PID: {pid}, Name: {name}")

    # Kill a sample process (replace 1234 with an actual PID)
    # manager.kill_process(1234)

    # Monitor memory usage every 2 seconds
    # manager.monitor_memory_usage(2)
