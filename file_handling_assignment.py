# file_handling_assignment.py

# Task 1: File Creation
try:
    # Create a new text file in write mode
    with open("my_file.txt", "w") as file:
        # Write at least three lines of text to the file
        file.write("Hello, World!\n")
        file.write("This is my first file.\n")
        file.write("The year is 2024.\n")
    print("File created and data written successfully.")

# Task 4: Error Handling
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while creating the file: {e}")

finally:
    print("File creation attempt complete.")

# Task 2: File Reading and Display
try:
    # Read the contents of the file
    with open("my_file.txt", "r") as file:
        contents = file.read()
        print("\nContents of 'my_file.txt':")
        print(contents)

# Task 4: Error Handling
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while reading the file: {e}")

finally:
    print("File reading attempt complete.")

# Task 3: File Appending
try:
    # Open the file in append mode
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text
        file.write("Appending another line.\n")
        file.write("Here is another line.\n")
        file.write("This is the final line in my file.\n")
    print("Data appended successfully.")

# Task 4: Error Handling
except (FileNotFoundError, PermissionError) as e:
    print(f"An error occurred while appending to the file: {e}")

finally:
    print("File appending attempt complete.")
