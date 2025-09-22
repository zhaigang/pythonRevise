def calc( *, number_1, number_2,  method):
    if method == '*':
        return number_1 * number_2
    else:
        return number_1 + number_2
    
result = calc(number_1 = 5, number_2=6, method='*')
print(result)

# summarize
# 1. / after this sign, argument must be positional
# 2. * after thi sign, argument must give as named.