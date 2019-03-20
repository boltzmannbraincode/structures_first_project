# the third and final part of the lab, which involves searching in the file for some numbers
import os

def read_buffer_from_file():  # reads the desired buffer from the file_number-th file
    buffer = []
    global buffer_size
    global disk_access_counter
    global file_pointer
    if (file_pointer <= 99000):
        sorted_file = open("final_file", 'rb')
        sorted_file.seek(file_pointer)  # sets the beginning of our reading space on the file at position file_pointer
        byte_array = bytearray(sorted_file.read(buffer_size))  # reads buffer_size amount of bytes from the file
        file_pointer = file_pointer + 1000
        sorted_file.close()
        disk_access_counter = disk_access_counter + 1
        for i in range( buffer_size):  # fill the buffer from the file TODO CHECK (-1)
            buffer.append(byte_array[i])
        return buffer
    else:
        print("error while reading from file: file_pointer>99000")


file_pointer = 0
buffer_pointer = 0
buffer = []
buffer_size = 1000                                                                                                                                                                                 #
disk_access_counter = 0
found = 0
number_we_search = 19   # NUMBER WE ARE SEARCHING FOR

if os.path.exists("final__file"):  # check if there is an old existing file
  print("File found.Proceeding.")
else:
  print("There was no existing file...")

buffer = read_buffer_from_file()


while(found == 0):
    for i in range(1000):
        if buffer[i] == number_we_search :
            found = 1
            print("Number was found.Total disk_acess_times=" + str(disk_access_counter))
    buffer = read_buffer_from_file()
    if file_pointer > 99000:
        print("The number was not found")
        found = 1






