#8. Write a Python script to create a copy of a file.?
import shutil

original_filename = input("Enter the name of the original file: ")
copy_filename = input("Enter the name of the copy file: ")

shutil.copy(original_filename, copy_filename)

print(f"The file '{original_filename}' has been copied to '{copy_filename}'")


