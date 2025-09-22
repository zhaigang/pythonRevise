list_a = ['1', '2', 3, 4, [5, 6]]

for one_val in list_a:
    match type(one_val).__name__:
        case 'int':
            print('it is integer')
        case 'str':
            print('it is string')
        case 'list':
            print('list')