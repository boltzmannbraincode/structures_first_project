#second half of second part of the project

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
    final_file = open("final_file", "wb")
    final_file.write(buffer11)
    final_file.close()
