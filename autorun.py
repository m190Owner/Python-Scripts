# Run all Python scripts in a folder

# Import the required modules
import os

# Display a message to the user
print("This script will run all the Python scripts in a folder.")

# Prompt the user to continue
response = input("Would you like to continue? (y/n) ")

# If the user enters "y", continue the script
if response.lower() == "y":
  # Prompt the user to enter the path to the folder
  folder_path = input("Please enter the path to the folder containing the Python scripts: ")

  # Get the list of files in the folder
  file_list = os.listdir(folder_path)

  # Iterate over the list of files
  for filename in file_list:
    # Check if the file is a Python script
    if filename.endswith(".py"):
      # Get the full path to the script file
      file_path = os.path.join(folder_path, filename)

      # Run the script using the Python interpreter
      os.system("python {}".format(file_path))

# If the user enters "n", exit the script
else:
  print("Exiting script.")
