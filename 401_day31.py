#!/usr/bin/python3

#In Python, write a script that will:

    # Prompt the user to type in a file name to search for.
    # Prompt the user for a directory to search in.
    # Search each file in the directory by name.

    # For each positive detection, print to the screen the file name and location.
    # At the end of the search process, print to the screen how many files were searched and how many hits were found.
    # The script must successfully execute on both Ubuntu Linux 20.04 Focal Fossa and Windows 10.

# Import libraries
import os
import platform
import subprocess

# Define variables
my_os = platform.system()
print(my_os)


# Define functions. Note: ChatGPT was used to help with the functions (specifically the subprocess module and "os.path.join")
def linux_search():
    file = input("Please enter the name of the file you want to find: ")
    filepath = input("Please enter the full filepath to search in: ")

    command = ["find", filepath, "-name", file]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, check=True)
        if result.stdout:
            print("File found at:")
            print(result.stdout)
        else:
            print("File not found.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

def windows_search():
    file = input("Please enter the name of the file you want to find: ")
    filepath = input("Please enter the full filepath to search in: ")

    command = ["dir", "/b", "/s", os.path.join(filepath, file)]

    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        if result.stdout:
            print("File found at:")
            print(result.stdout)
        else:
            print("File not found.")
    except subprocess.CalledProcessError as e:
        print("An error occurred:", e)

# Main

if my_os == "Linux":
    linux_search()
elif my_os == "Windows":
    windows_search()
else:
    print("Your OS is not compatible")
      
# End

