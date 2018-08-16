def say_yeah(name, age):
    print("やあ、 " + name + "。あなたは、" + str(age) + "歳だったよね。")


say_yeah("かずき",41)
say_yeah("きん",109)

def cube(num):
    return num*num*num


result = cube(5)
print(result)


def exception_test(value_1, value_2):

    print('☆☆開始☆☆')

    result = 0

    try:
        result = value_1 + value_2
    except:
        print('出来ませんでした！')
        raise
    finally:
        print('終了！！')
    return result
     
try: 
    print(exception_test(200, 200))
    print(exception_test(400, 300))
    print(exception_test('100', 300))
except:
    print('エラー')


import sys
import traceback
 
def exception_test2(value_3, value_4):
 
    print('開始')
 
    result = 0
 
    try:
        result = value_3 + value_4
    except:
        print('出来ませんでした！')
        raise
    finally:
        print('終了')
 
    return result
     
 
try:
    print(exception_test2(300, 500))
except:
    print('---------------------------------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('---------------------------------------')