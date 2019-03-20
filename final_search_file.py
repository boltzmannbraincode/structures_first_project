# the third and final part of the lab, which involves searching in the file for some numbers
import os
import random

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
        for i in range(buffer_size):  # fill the buffer from the file TODO CHECK (-1)
            buffer.append(byte_array[i])
        return buffer
    else:
        print("error while reading from file: file_pointer>99000")

def serial_search_file(number_we_search,):  # used to search the entire file at once using serial(sequential) search
    found = 0
    global file_pointer
    file_pointer = 0  # it is returned to zero to avoid exceeding the limits of the file
    buffer = read_buffer_from_file()
    while (found == 0):
        for i in range(1000):
            if buffer[i] == number_we_search:
                found = 1
        buffer = read_buffer_from_file()
        if file_pointer > 99000:
            print("The number was not found")
            return 1
    if found == 1 :
        print("Number found!")

def serial_search_buffer(number_we_search,buffer):
    found = 0
    global buffer_size
    for i in range(buffer_size):
        if buffer[i] == number_we_search:
            found = 1
    return found  # if search was successful, it returns 1

def binary_search(number_we_search):  # file length in bytes is used to determine how many buffers there are to examine
    global file_pointer
    global buffer_size
    beginning = 0  # beginning buffer number
    end =  int(100000/buffer_size)  # ending buffer number.100000 is the size of the file in bytes
    found = False
    while beginning<=(end-3) and not found:
        midpoint = (beginning + end)//2
        file_pointer = midpoint*buffer_size
        midpopint_buffer = read_buffer_from_file()

        if serial_search_buffer(number_we_search,midpopint_buffer) == 1:
             found = True
             print("Number found using binary search!")
        else:
             if number_we_search < min(midpopint_buffer):
                  end = midpoint-1
             else:
                  beginning = midpoint+1
    if found == False :
        print("Number was NOT found using binary search!")
    return found

# essential variables initialisation (some are used as global in the functions)
file_pointer = 0
buffer_pointer = 0
buffer = []
buffer_size = 1000
disk_access_counter = 0

if os.path.exists("final_file"):  # check if there is an old existing file
    print("File found.Proceeding.")
else:
    print("There was no existing file, the program will be terminated.Run again the previous ")
    print("Python scripts ( filemaker.py, filesort.py and filesort_merge.py).")
    exit()  # terminates the program

# test serial search
print("Attempting serial search...")
for a in range(8):
    random_int = random.randint(1,100)
    serial_search_file(random_int)

avg_disk_access_counter_serial = disk_access_counter/40

disk_access_counter = 0

# test binary search
print("Attempting binary search..." )
for i in range(40):
    random_integer = random.randint(1,100)
    binary_search(random_integer)

avg_disk_access_counter_binary = disk_access_counter/40
print("Average disk access count with binary search: " + str(avg_disk_access_counter_binary))
print("Average disk access count with serial search: " + str(avg_disk_access_counter_serial) + "\n")




