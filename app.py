import os
import requests

# Insecure function that takes a command from user input for execution
def execute_command(user_input):
    # Using os.system with user input is a security risk
    os.system(user_input)

# Function vulnerable to Server-Side Request Forgery (SSRF)
def fetch_url(user_url):
    # Directly using user input to make a web request
    response = requests.get(user_url)
    return response.text

# Example usage of the insecure functions
execute_command("ls")  # Example of command execution vulnerability
print(fetch_url("http://example.com"))  # Example of SSRF vulnerability
