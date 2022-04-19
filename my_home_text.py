variable_1 = 'my'
variable_2 = 'duty'
variable_3 = 'is'
variable_4 = 'done'

filename = 'text.txt'
with open(filename, 'a') as file_object:
    file_object.write('is\n')
    file_object.write('done\n')
    file_object.close()
