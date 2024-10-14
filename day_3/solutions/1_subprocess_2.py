import asyncio
import nest_asyncio

# Allow nested event loops
nest_asyncio.apply()

async def run_command(command):
    process = await asyncio.create_subprocess_exec(*command, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await process.communicate()
    
    return stdout.decode().strip(), stderr.decode().strip()

async def main():
    commands = [["echo", "Hello"], ["sleep", "2"], ["echo", "World"], ["ls", "non_existent_directory"]]
    tasks = [run_command(cmd) for cmd in commands]
    
    results = await asyncio.gather(*tasks)
    
    for i, (stdout, stderr) in enumerate(results):
        print(f"Command {i + 1}:")
        print(f"Output: {stdout}")
        print(f"Error: {stderr if stderr else 'No errors'}")
        print("-----")

# Run the main function
asyncio.run(main())
