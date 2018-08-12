test_dict_1 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_1)

print('=================================')

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('-----------------------------')

test_dict_2 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_2)

print('==================================')

print(test_dict_2['YEAR'])
#print(test_dict_2['YEARS'])

print('==================================')

print(test_dict_2.get('YEAR'))
print(test_dict_2.get('YEARS'))

print('==================================')

print(test_dict_2.get('YEAR','NOT FOUND'))
print(test_dict_2.get('YEARS','NOT FOUND'))

test_dict_3 = {}

print(test_dict_3)

print('==================================')

test_dict_3['YEAR'] = '2018'
test_dict_3['MONTH'] = '8'
test_dict_3['DAY'] = '12'

print(test_dict_3)

test_dict_4 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_4)

print('==================================')

del test_dict_4['DAY']

print(test_dict_4)

test_dict_5 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_5)

print('==================================')

print(test_dict_5.keys())
print(test_dict_5.values())

test_dict_6 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_6)

print('==================================')

for key, value in test_dict_6.items():
    print(key, value)

test_dict_7 = {'YEAR':'2018', 'MONTH':'8', 'DAY':'12'}

print(test_dict_7)

print('==================================')

print('YEAR' in test_dict_7)
print('YEARS' in test_dict_7)