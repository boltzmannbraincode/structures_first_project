#this is the first half of the second part of the project. it taces the created file, and splits it to 10 sorted files

import os  # used to remove an old file

number_file = open('number_file', 'rb')
byte_array = bytearray(number_file.read())  # TODO: change it so that it loads only the buffer size
#  this byte_array is the simulation of the file
file_pointer = 0  # a "pointer" to keep our position in the "file"(NOT in the 10,000 array)
array_to_sort = []  # initialise an empty list
buffer_size = 1000

for l in range(10):
    for i in range(10):
        buffer = [int(byte_array[x]) for x in range(file_pointer,(file_pointer + buffer_size))]  # this buffer consists of integers
        file_pointer = file_pointer + buffer_size  # move our position(RETAINS ITS VALUE ON THE OUTER LOOP)
        for index in range(buffer_size):  # fill the buffer with the array_to_sort contents
            array_to_sort.append(buffer[index])

    array_to_sort.sort()  # sorts the 10,000 array
    sorted_array = array_to_sort
    filename = "sorted_file" + str(l)  # creates the name of the l-th sorted file(the outer loop!, not htis one)
    if os.path.exists(filename):  # check if there is an old existing file...
        os.remove(filename)  # ...and delete it
        print("deleted old " + filename + ",  " , end = '')
    sorted_file = open(filename, 'a+b')  # create i-th sorted file and name it accordingly
    array_pointer = 0  # a pointer that shows position inside 10,000 cell array

    for k in range(10):  # write 10 buffers to each of the 10 files
        buffer = []
        for x in range(array_pointer, (array_pointer + buffer_size)):  # take the first,second,etc, 1000 elements of sorted_array
            buffer.append(sorted_array[x])
        array_pointer = array_pointer + buffer_size  # this array pointer is retained through this loop(k loop)
        byte_buffer = bytearray(buffer)  # convert the buffer to bytearray
        sorted_file.write(byte_buffer)  # writes(appends) the buffer to the i-th sorted file
    print("created new " + filename )
    sorted_file.close()
print("Done.")

filename_to_test = "sorted_file0"  # change file name to test a different file
print("Testing " + filename_to_test +"... \n")
print("Printing first 100 numbers... ")
number_file = open(filename_to_test, 'rb')
byte_array = bytearray(number_file.read())
for i in range(100):
    print(str(int(byte_array[i])) + "," , end = '')
print("\nIf the numbers seem sorted, chances are that the sorting was successful.")







