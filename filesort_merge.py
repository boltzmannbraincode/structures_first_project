#second half of second part of the project
N = 100000  # amount of numbers that we work with

def read_buffer_from_file(file_number,file_pointer,buffer_size):  # reads the desired buffer from the file_number-th file
    buffer = []
    if (file_pointer < 9000):
        filename = "sorted_file" + str(file_number)
        sorted_file = open(filename, 'rb')
        sorted_file.seek(file_pointer)  # sets the beginning of our reading space on the file at position file_pointer
        byte_array = bytearray(sorted_file.read(buffer_size))  # reads buffer_size amount of bytes from the file
        sorted_file.close()
        for i in range(file_pointer, file_pointer + buffer_size):  # fill the buffer from the file
             buffer.append(byte_array[i])
        return buffer
    else:
        print("error while reading from file: file_pointer>9000")


def write_buffer11_to_file(buffer11):
    final_file = open("final_file", "ab")
    byte_buffer11 = bytearray(buffer11)
    final_file.write(byte_buffer11)
    final_file.close()

#############################################################################################################
file_pointer = [0 for a in range(10)]                                                                       #
buffer_pointer = [0 for b in range(10)]                                                                     #
buffer = [[] for c in range(10)]                                                                            #
buffer_size = 1000                                                                                          #
list_of_files = [0,1,2,3,4,5,6,7,8,9]                                                                       #
position_of_min_val = 0                                                                                     #
buffer11 = []                                                                                               #
disk_access_counter = 0                                                                                     #
#############################################################################################################

for initial_fill_counter in range(10):  # initialise all the buffers once
    buffer[initial_fill_counter] = read_buffer_from_file(initial_fill_counter,file_pointer[initial_fill_counter],buffer_size)
    disk_access_counter = disk_access_counter + 1
    file_pointer[initial_fill_counter] = file_pointer[initial_fill_counter] + buffer_size



# M A I N   B I G   L O O P
for main_counter in range(N):
    min_val = buffer[list_of_files[0]][0]  # initialise with the first element of the first buffer that exists in the available files
    #finds the lesser value from the buffers
    for min_val_counter in list_of_files:
        if buffer[min_val_counter][buffer_pointer[min_val_counter]] < min_val:
            min_val = buffer[min_val_counter][buffer_pointer[min_val_counter]]
            buffer_pointer[min_val_counter] = buffer_pointer[min_val_counter] + 1
            position_of_min_val = min_val_counter

    # IMPORTAND: the only change is hapening to buffer No. position_of_min_val, so from now on we only use that variable on our checks.
    # CHECKS if the current file/buffer is emptied
    if buffer_pointer[position_of_min_val] == 1000:  # if the buffer is "empty"
        if file_pointer[position_of_min_val] < 10000:
            buffer[position_of_min_val] = read_buffer_from_file(position_of_min_val,file_pointer[position_of_min_val],buffer_size)
            buffer_pointer[position_of_min_val] = 0
            file_pointer[position_of_min_val] = file_pointer[position_of_min_val] + buffer_size
        else:
            list_of_files.remove(position_of_min_val)
            print("Removed sorted_file" + str(position_of_min_val) + " from file list.")

    buffer11.append(buffer[position_of_min_val][buffer_pointer[position_of_min_val]])  # adds the minimum value to the buffer11
    # checks if the buffer11 is full to write it to the final file and empty it
    if len(buffer11) == buffer_size :
        write_buffer11_to_file(buffer11)
        disk_access_counter = disk_access_counter + 1
        buffer11.clear()

print("Total disk_acces_counter=" + str(disk_access_counter))

filename_to_test = "final_file"  # change file name to test a different file
print("Testing " + filename_to_test +"... \n")
print("Printing first 1000 numbers... ")
number_file = open(filename_to_test, 'rb')
byte_array = bytearray(number_file.read())
for i in range(10000):
    print(str(int(byte_array[i])) + "," , end = '')
print("\nIf the numbers seem sorted, chances are that the sorting was successful.")






