#second half of second part of the project
import os
N = 100000  # amount of numbers that we work with

def read_buffer_from_file(file_number,file_pointer,buffer_size):  # reads the desired buffer from the file_number-th file
    buffer = []
    if (file_pointer <= 9000):
        global disk_access_counter
        filename = "sorted_file" + str(file_number)
        sorted_file = open(filename, 'rb')
        sorted_file.seek(file_pointer)  # sets the beginning of our reading space on the file at position file_pointer
        byte_array = bytearray(sorted_file.read(buffer_size))  # reads buffer_size amount of bytes from the file
        sorted_file.close()
        disk_access_counter = disk_access_counter + 1
        for i in range( buffer_size):  # fill the buffer from the file TODO CHECK (-1)
            buffer.append(byte_array[i])
        return buffer
    else:
        print("error while reading from file: file_pointer>9000")


def write_buffer11_to_file(buffer11):
    global disk_access_counter
    final_file = open("final_file", "ab")
    byte_buffer11 = bytearray(buffer11)
    final_file.write(byte_buffer11)
    disk_access_counter = disk_access_counter + 1
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
temp_list = [0 for d in range(10)]                                                                          #
#############################################################################################################

for initial_fill_counter in range(10):  # initialise all the buffers once
    buffer[initial_fill_counter] = read_buffer_from_file(initial_fill_counter,file_pointer[initial_fill_counter],buffer_size)
    file_pointer[initial_fill_counter] = file_pointer[initial_fill_counter] + buffer_size

if os.path.exists("final_file"):  # check if there is an old existing file...
    os.remove("final_file")  # ...and delete it
    print("deleted old final_file.")

# M A I N   B I G   L O O P
for main_counter in range(N):
    for i in list_of_files:
        temp_list[i] = buffer[i][buffer_pointer[i]]

    # now temp_list holds all the numbers that need to be compared(CONFIRMED!)
    min_val = min(temp_list)

    print("MinVal= " + str(min_val))
    position_of_min_val = temp_list.index(min_val)

    # increase buffer pointer
    buffer_pointer[position_of_min_val] = buffer_pointer[position_of_min_val] + 1

    # write to buffer11
    buffer11.append(min_val)

    # check buffer11
    if len(buffer11) == buffer_size :
        write_buffer11_to_file(buffer11)
        buffer11.clear()

    # check bufferX
    if buffer_pointer[position_of_min_val] == (buffer_size - 1):
        buffer[position_of_min_val] = read_buffer_from_file(position_of_min_val,file_pointer[position_of_min_val],buffer_size)
        file_pointer[position_of_min_val] = file_pointer[position_of_min_val] + buffer_size
        buffer_pointer[position_of_min_val] = 0

    # check fileX
    if file_pointer[position_of_min_val] >=10000:
        print("position_of_min_val" + str(position_of_min_val))
        try:
            list_of_files.remove(position_of_min_val)
        except:
            print("Removed a file...")
        filename = "sorted_file" + str(position_of_min_val)



print("\n\n\nTotal disk_access_counter = " + str(disk_access_counter))


################################################### T E S T ########################################################
filename_to_test = "final_file"  # change file name to test a different file
print("\nTesting " + filename_to_test +"... \n")
print("\nPrinting first 1000 numbers... ")
number_file = open(filename_to_test, 'rb')
byte_array = bytearray(number_file.read())
for i in range(10000):
    print(str(int(byte_array[i])) + "," , end = '')
print("\nIf the numbers seem sorted, chances are that the sorting was successful.")
