number_file = open('number_file', 'rb')
byte_array = bytearray(number_file.read())  # TODO: change it so that it loads only the buffer size
#  this byte_array is the simulation of the file
file_pointer = 0  # a "pointer" to keep our position in the "file"
array_to_sort = []  # initialise an empty list

for l in range(10):
    for i in range(10):
        buffer = [int(byte_array[x]) for x in range(file_pointer,(file_pointer + 1000))]  # this buffer consists of integers
        file_pointer = file_pointer + 1000  # move our position(RETAINS ITS VALUE ON THE OUTER LOOP)
        for index in range(1000):
            array_to_sort.append(buffer[index])

    sorted_array = array_to_sort.sort()

    for k in range(10):
        buffer = []
        array_pointer = 0  # a pointer that shows position inside 10,000 cell array
        for x in range(array_pointer, (array_pointer + 1000)):
            buffer.append(sorted_array[x])
            array_pointer = array_pointer + 1000
        filename = "sorted_file" + str(l)  # creates the name of the l-th sorted file(the outer loop!, not htis one)
        sorted_file = open(filename, 'a+b')  # create i-th sorted file and name it accordingly
        sorted_file.write(buffer)  # writes(appends) the buffer to the i-th sorted file







