import os

# Insecure function that takes a command from user input
def execute_command(user_input):
    # Using os.system with user input is a security risk
    os.system(user_input)

# Example usage of the insecure function
execute_command("ls")
