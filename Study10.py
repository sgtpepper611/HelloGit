test_list_1 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_1[:])
print(test_list_1[::])

test_list_2 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_2[:4])

test_list_3 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_3[2:])

test_list_4 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_4[::2])

test_list_5 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_5[3:5])

test_list_6 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_6[-1:])   # 末尾から全ての要素
print(test_list_6[:-1])   # 末尾まで全ての要素
print(test_list_6[::-1])  # 末尾から全ての逆順要素

test_list_7 = ['https', 'www', 'python', 'sgt', 'com']
 
print(test_list_7[:800])

test_list_8 = ['https', 'www', 'python', 'sgt', 'com']
 
test_list_8[1:3] = ('WWW', 'PYTHON') #要素の代入
 
print(test_list_8)