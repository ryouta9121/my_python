names = ["今西","佐藤","鈴木","高橋","川上"]

# print(names[0] + "さん")
# print(names[1] + "さん")
# print(names[2] + "さん")
# print(names[3] + "さん")
# print(names[4] + "さん")

# for i in range():
#     print(names[i] + "さん")


# for i in range(len(names)):
#     print(names[i] + "さん")

# for num in range(20):
#     print (num + 1)

# sum = 0
# for num in range(20):
#     sum +=(num + 1)

# print(sum)

# for name in names:
#     print(name + "さん")

last_names = ["今西","佐藤","鈴木","田中"]
first_names = ["航平","謙介","康二","康介"]

# print((last_name[0])+(first_name[0]) + "さん")
# print((last_name[1])+(first_name[1]) + "さん")
# print((last_name[2])+(first_name[2]) + "さん")
# print((last_name[3])+(first_name[3]) + "さん")

# for i in range(len(last_names)):
#     print(last_names[i] + first_names[i] + "さん")

# for last_name, first_name in zip(last_names,first_names):
#     print(last_name + first_name + "さん")

# print("出席番号",0,"番目の" + last_names[0] + "さん")
# print("出席番号",1,"番目の" + last_names[1] + "さん")
# print("出席番号",2,"番目の" + last_names[2] + "さん")
# print("出席番号",3,"番目の" + last_names[3] + "さん")

# for i in range(len(last_names)):
#     print("出席番号",i,"番目の" + last_names[i] + "さん")

# for num, last_name in enumerate(last_names):
#     print("出席番号",num,"番目の" + last_name + "さん")


for l_name, f_name in zip(last_names,first_names):
    print(l_name + f_name + "さん")