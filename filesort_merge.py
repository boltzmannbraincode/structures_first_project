# this is the second half of the second part of the project
import os

buffer_size = 1000

def read_buffer_from_file(file_number,buffer_number):  # reads the desired buffer from the file_number-th file
    buffer = []
    filename = "sorted_file" + str(file_number)
    sorted_file = open(filename, 'rb')
    byte_array = bytearray(sorted_file.read())  # TODO: read only the desired buffer from file
    sorted_file.close()
    if (buffer_number<9000):
        for i in range(buffer_number, buffer_number + buffer_size):  # fill the buffer from the file
            buffer.append(byte_array[i])
    return buffer

# define the buffers of the sorted_files
buffers = [[] for i in range(10)]  # defines a list of lists
# define the buffer to be written
buffer11 = [] # bufferELEVEN not buferll
#define the buffer11 pointer, to keep our position in it
buffer11_pointer = 0
#define the file "pointers" of the sorted_files
file_pointers = [0 for a in range(10)] # each time it will be increased by buffer_size
# define the buffer "pointers" (to show our position in each of the 10 buffers)
buffer_pointers = [0 for b in range(10)]  # each time it is increased by 1
list_of_files = [0,1,2,3,4,5,6,7,8,9]  # the list of files.later some files will be removed

if os.path.exists("final_sorted_file"):  # check if there is an old existing file...
    os.remove("final_sorted_file")  # ...and delete it
    print("deleted old final_sorted_file. ")

for i in range(10):  # initially fill each buffer once
    buffers[i] = read_buffer_from_file(i, 0)  # fill the i-th buffer from the beginning of the file(hence the 0)
    file_pointers[i] = file_pointers[i] + buffer_size  # increment the file pointer by buffer_size

print("Sorting, please wait...")
for n in range(100000):
    min_value = buffers[0][buffer_pointers[0]]
    buffer_of_smallest_value = 0  # variable to keep the origin buffer of the smaller value
    for x in list_of_files:  # fill the temp_buffer with the first of each sorted_file buffer
        # buffer_pointers[x]-th of buffers[x](the x-th buffer), FIND LESSER VALUE
        if buffers[x][buffer_pointers[x]] < min_value:  # if the current value is smaller than the previous, and if it is,it is set as min_value
            min_value = buffers[x][buffer_pointers[x]]
            buffer_of_smallest_value = x  # it keeps the buffer number that the smallest number came from, to increment its buffer_pointer later
        buffer_pointers[buffer_of_smallest_value] = buffer_pointers[buffer_of_smallest_value] + 1

        if (buffer_pointers[x] >= buffer_size-2):  # if we reached the end of a buffer
            read_buffer_from_file(x, file_pointers[x])  # renew the emptied x-th buffer
            buffer_pointers[x] = 0  # re-initialise the buffer "pointer" to zero
        #print(buffer_pointers[x])  # TODO: remove this Debug-print()

    buffer11.append(min_value)  # keep the minimum value of the 10 in the 11th buffer
    buffer11_pointer = buffer11_pointer + 1  # increment our position in the buffer11 list

    byte_buffer11 = bytearray(buffer11)
    if (buffer11_pointer>=buffer_size):  # if the buffer 11 is full...
        final_file = open('final_sorted_file', 'a+b')  # ...open the final file...
        final_file.write(byte_buffer11)  # ...write buffer 11 in it...
        final_file.close()  # ...close it...
        buffer11.clear()  # ...empties the buffer 11...
        buffer11_pointer = 0  # ...and re-initialises to zero its "pointer".'
        file_pointers[buffer_of_smallest_value] =  file_pointers[buffer_of_smallest_value] + buffer_size  # change our "position" in the file
        if (file_pointers[buffer_of_smallest_value] >= 10000):
            print(buffer_of_smallest_value)  # TODO remove
            list_of_files.remove(buffer_of_smallest_value)



# T E S T  S E C T I O N
filename_to_test = "final_sorted_file"  # change file name to test a different file
print("Testing " + filename_to_test +"... \n")
print("Printing first 1000 numbers... ")
number_file = open(filename_to_test, 'rb')
byte_array = bytearray(number_file.read())
for i in range(1000):
    print(str(int(byte_array[i])) + "," , end = '')
print("\nIf the numbers seem sorted, chances are that the sorting was successful.")












