print('python-sgt')

print("python-sgt")

test_str = """
test_1
test_2
"""
print(test_str)

test_str = 'python'
test_str = test_str + '_'
test_str = test_str + 'sgt'

print(test_str)

test_str = '012' * 3
test_str += '345'
test_str += '678'
test_str += '9'

print(test_str)

test_integer = 100

print(str(test_integer) + '円')

test_str = 'python-sgt'

print(test_str.replace('sgt', 'sjt'))

test_str = 'python-sgt'

print(test_str.split('-'))

test_str = '1234'

print(test_str.rjust(10, '0'))
print(test_str.rjust(10, '!'))

test_str = '1234'

print(test_str.zfill(10))
print(test_str.zfill(3))

test_str = 'python-sgt'

print(test_str.startswith('python'))
print(test_str.startswith('sgt'))

test_str = 'Python-sgt.Com'

print(test_str.upper())
print(test_str.lower())

print('----------------------------------------')

test_str = '                python-sgt.com'
print(test_str)

test_str = test_str.lstrip()
print(test_str)

test_str = test_str.lstrip('python')
print(test_str)

print('-----------------------------------------')

test_str = 'python-sgt.com      '
print(test_str + '/')

test_str = test_str.rstrip()
print(test_str + '/')

test_str = test_str.rstrip("com")
print(test_str)