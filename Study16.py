value = 3
 
if value == 1:
    print('valueの値は1です')
elif value == 2:
    print('valueの値は2です')
elif value == 3:
    print('valueの値は3です')
else:
    print('該当する値はありません')


value_1 = 'python'
value_2 = 'sgt'
 
if value_1 == 'Python':
    pass
elif value_1 == 'python' and value_2 == 'sgt':
    print('2番目の条件式がTrue')
elif value_1 == "SGT" or value_2 == "PYTHON":
    print('3番目の条件式がTrue')


value_1 = 'python'
value_2 = 'sgt'
 
if value_1 == 'Python':
    pass
elif value_1 == 'python' and value_2 == 'sgt':
    print('2番目の条件式がTrue')
elif value_1 == "SGT" or value_2 == "PYTHON":
    print('3番目の条件式がTrue')

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You neither not male or not tall or both")
