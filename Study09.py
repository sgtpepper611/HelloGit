test_set_1 = {'python', '-', 'izm', '.', 'com'}
print(test_set_1)

print('--------------------------------')

for i in test_set_1:
    print(i)

# これはディクショナリ
test_dict = {}

# これはセット
test_set = {'python'}

# 空のセットは「set」を使う
empty_set = set()

test_set_2 = {'python', '-', 'izm', '.', 'com', 'python', 'izm'}

print('--------------------------------')

for i in test_set_1:
    print(i)

test_set_3 = set()

test_set_3.add('python')
test_set_3.update({'-', 'izm', '.', 'com'})
 
print(test_set_3)

test_set_4 = {'python', '-', 'izm', '.', 'com'}
 
test_set_4.remove('-')
test_set_4.discard('.')
 
print(test_set_4)

test_set_5 = frozenset({'python', '-', 'izm', '.', 'com'})
 
# test_set_5.remove('-') はAttributeErrorが発生する。
# test_set_5.discard('.')はAttributeErrorが発生する。
 
print(test_set_5)