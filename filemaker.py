#this is the first part of the project.it creates a binary file with N numbers

import random  # used to generate random number
import os  # used to remove an old file
N = 100000  # total amount of number

if os.path.exists("number_file"):  # check if there is an old existing file
  os.remove("number_file")
  print("I deleted an old existing file.")
else:
  print("There was no existing file, continuing...")

number_file = open('number_file', 'a+b')  # open/create the file

for i in range (int(N/1000)):
    buffer = [random.randint(1, 200) for x in range(1000)]  # make an array of 1000 random elements
    binary_format_buffer = bytearray(buffer)  # cast the integer array to bytearray
    number_file.write(binary_format_buffer)
print("Wrote " + str(1000) + " bytes, " + str(int(N/1000)) + " times.")
number_file.close()
