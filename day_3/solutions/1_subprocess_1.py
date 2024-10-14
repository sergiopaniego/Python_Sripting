import subprocess

def capture_command_output(command):
    try:
        # Run the command and capture output
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        # Write standard output to a file
        with open("output.log", "w") as out_file:
            out_file.write(result.stdout)
        
        print("Standard output captured in 'output.log'.")
    
    except subprocess.CalledProcessError as e:
        # Write standard error to a file
        with open("error.log", "w") as err_file:
            err_file.write(e.stderr)
        
        print("An error occurred. Error message captured in 'error.log'.")

# Example command (you can change it to any command)
command = ["ls"]  # This will cause an error
capture_command_output(command)