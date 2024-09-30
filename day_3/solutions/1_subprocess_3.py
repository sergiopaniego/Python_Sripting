import os
import subprocess

def run_command_with_modified_env(command, new_path):
    # Copy current environment variables
    my_env = os.environ.copy()
    # Modify the PATH environment variable
    my_env["PATH"] = new_path + ":" + my_env["PATH"]

    try:
        result = subprocess.run(command, env=my_env, check=True, capture_output=True, text=True)
        print(f"Command executed successfully: {result.stdout}")
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e.stderr}")

# Example command (e.g., you can test with 'echo $PATH' if using bash)
command = ["echo", "$PATH"]  # Note: To see the PATH in the modified environment, consider using 'env' or a script that can interpret it.
new_path = "/custom/path"  # Example new path
run_command_with_modified_env(command, new_path)
