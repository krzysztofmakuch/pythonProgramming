def input_function():
    ''' '''
    input_data = input('Podaj jakiegos stringa: ')
    #list from string:
    L = list(input_data)
    length_of_input = len(L)
    print('%25s %29s' %('Podales takiego stringa:', 'Uzyjemy takiej listy'))
    print('%25s %29s' %(input_data, L))
    
    print('\npetla for ze skladnia C: ')
    print('slowo:')
    for_C_like(input_data, length_of_input)
    print('lista:')
    for_C_like(L, length_of_input)
    
    print('\npetla for ze skladnia pythonowa: ')
    print('slowo:')
    for_python_style(input_data, length_of_input)
    print('lista:')
    for_python_style(L, length_of_input)

    print('\npetla while: ')
    print('slowo:')
    while_loop(input_data, length_of_input)
    print('lista:')
    while_loop(input_data, length_of_input)
    
def for_C_like(data, data_len):
    ''' '''
    for i in range(0,data_len):
        print(data[i])


def for_python_style(data, data_len):
    ''' '''
    for word in data:
        print(word)


def while_loop(data, data_len):
    ''' '''
    i = 0
    while i < data_len:
        print(data[i])
        i += 1
