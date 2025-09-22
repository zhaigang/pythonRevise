list_a = [1,2,3]
list_b = ['1', '2','3']
print([one_value for one_value in zip(list_a, list_b)])
print({one_list_a_value: one_list_b_value for one_list_a_value, one_list_b_value in zip(list_a, list_b)})

list_c = ['c1', 'c2','c3', 'c4']

print([one_value for one_value in zip(list_a, list_c)])
print([one_value for one_value in zip(list_c, list_a)])

list_d = [1, 2,3,4,2]
print(list(set(list_d)))


