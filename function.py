# def say_hello():
#     print("みなさん、こんにちわ。")
 
# say_hello()


# def say_hello2(name):
#     print("{}さん、こんにちわ。".format(name))

# say_hello2("今西")




# def calc_square(side):
#     return side*side

# result = calc_square(10)
# print(result)


# 例外処理について
# def calc_tri(base,height):
#     return base*height*0.5

# base = 10
# height = "5"

# try:
#     result = calc_tri(base,height)
#     print("計算結果:{}".format(result))
# except Exception as e:
#     print("計算できません")
#     print(e)


try:
    a = 10
    b = 1
    result = a/b
except ZeroDivisionError:
    print("0で割ってます")
finally:
    print("ここは必ず通ります")