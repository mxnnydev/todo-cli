import os

# Utility functions for file operations in the To-Do List Manager
def task_exists(filename):
    if os.path.exists(filename):
        return True
    return False
