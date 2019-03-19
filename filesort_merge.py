# this is the second half of the second part of the project
buffer_size = 1000

def read_buffer_from_file(file_number,buffer_number):  # reads the desired buffer from the file_number-th file
    buffer = []
    filename = "sorted_file" + str(file_number)
    sorted_file = open(filename, 'rb')
    byte_array = bytearray(sorted_file.read())  # TODO: read only the desired buffer from file
    sorted_file.close()
    for i in range(buffer_number, buffer_number + buffer_size):  # fill the buffer from the file
        buffer.append(byte_array[i])
    return buffer

# define the buffers of the sorted_files
buffers = [[] for i in range(10)]  # defines a list of lists
# define the buffer to be written
buffer11 = []  # bufferELEVEN not buferll

#define the file "pointers" of the sorted_files
file_pointers = [0 for a in range(10)] # each time it will be increased by buffer_size
# define the buffer "pointers" (to show our position in each of the 10 buffers)
buffer_pointers = [0 for b in range(10)]  # each time it is increased by 1
temp_buffer = [0 for c in range(10)]  # a temporary buffer to hold the first value of each buffer in order to find the smaller

for i in range(10):  # initially fill each buffer once
    buffers[i] = read_buffer_from_file(i,0)  # fill the i-th buffer from the beginning of the file(hence the 0)
    file_pointers[i] = file_pointers[i] + buffer_size  # increment the file pointer by buffer_size

for x in range(10):  # fill the temp_buffer with the first of each sorted_file buffer
    # temp_buffer[x] = buffer_pointers[x]-th of buffers[x](the x-th buffer)
    temp_buffer[x] = buffers[x][buffer_pointers[x]]
    



