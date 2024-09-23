import sys

# Open a file in write mode to redirect stderr
file = open("error_output.txt", "w")
sys.stderr = file

a = 5
b = 0

print(a / b)

file.close()

# Check Content of error_output.txt file.