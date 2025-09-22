list_a = [1, 2]
print(list_a)
list_a.append('3')
print(list_a)
list_a.insert(1, '1')
print(list_a)
list_a.remove(2)
print(list_a)
list_a.pop()
print(list_a)
list_a.pop(0)
print(list_a)
print(list_a.count('1'))


list_b = [1, 2, 3, 4, 6]
list_b_square = [one*one for one in list_b]
print(list_b_square)

list_b_square_filted = [one*one for one in list_b if one % 2 == 0]
print(list_b_square_filted)

def delete_one_resource(resource_id):
    print('delete it:%s' % resource_id)
resouce_list= ['ecs_1', 'ecs_2', 'ecs_3']
[delete_one_resource(one) for one in resouce_list]