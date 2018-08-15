print('python')
print('-')
print('sgt')
print('.com')


print('python', end=' ')
print('-', end=' ')
print('sgt', end=' ')
print('.com')


f_obj = open('test.com', 'w')
print('python-sgt.com', file=f_obj)


print('Python : %s' % 'python-sgt.com')
print('Python : %s-%s.%s' % ('python', 'sgt', 'com'))
 
test_int = 500 + 500
test_str = 'python-sgt.com'
print('今日は開設 %d 日目！ %s' % (test_int, test_str))
