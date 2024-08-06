# Question 1 Task 1 

import os

def list_directory_contents(path):
    try:
        for root, dirs, files in os.walk(path):
            print(f"Root Directory: {root}")
            print("Subdirectories:")
            for dir in dirs:
                print(f" - {dir}")
            print("Files:")
            for file in files:
                print(f" - {file}")
            print("\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    directory_path = input("Enter the directory path: ").strip()
    if os.path.isdir(directory_path):
        list_directory_contents(directory_path)
    else:
        print("The specified path is not a valid directory.")
