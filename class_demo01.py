
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
    j = 987






class Bird:
    '这是学习python的第一个类'
    eyes = "two"
    def __init__(self, color,feet):  # '为python对象增                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '
        self.color = color
        self.feet = feet
    def call(self,cd):
        print("This bird:",cd)



class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

class newClass:
    def __init__(self, abc):
        self.a = abc




def test():

    print("Test !!! ")

    xique = Bird("green", "two")
    xique.call("gezhi")





def test_02():

    # 实例化类
    x = MyClass()

    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)
    print("yClass 类的属性 j 为：", x.j)
    print("MyClass 类的方法 f 输出为：", x.f())



def test_03_complex():
    x = Complex(3.0, -4.5)
    print(x.r, x.i)   # 输出结果：3.0 -4.5



def newClass_test():
    x = newClass(7)

    print(x.a)


if __name__ == '__main__':
    # test()

    # test_02()

    # test_03_complex()

    newClass_test()
