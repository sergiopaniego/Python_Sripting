def read_file():
    try:
        filename = input("Enter the filename: ")
        with open(filename, "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don't have permission to read the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Program execution completed.")

read_file()
