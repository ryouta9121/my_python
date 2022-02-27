from unicodedata import name


class Person:
    def __init__(self,name,nationality,age):
        self.name = name
        self.nationality = nationality
        self.age = age

    def __call__(self):
        print("ここはcall関数です。")

    def say_hello(self,name):
        print("こんにちわ{}さん。私は{}です。".format(name,self.name))

yosikawa = Person("吉川","日本",29)
yosikawa.say_hello("佐藤")

maik = Person("マイク","アメリカ",13)
maik.say_hello("加藤")

yosikawa()
# print(yosikawa.name)

# maik = Person("マイク","アメリカ",13)
# print(maik.name,maik.nationality,maik.age)

