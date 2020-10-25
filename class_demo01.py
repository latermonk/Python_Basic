
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'






class Bird:
    '这是学习python的第一个类'
    eyes = "two"
    def __init__(self, color,feet):  # '为python对象增                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 '
        self.color = color
        self.feet = feet
    def call(self,cd):
        print("This bird:",cd)



def test():

    print("Test !!! ")

    xique = Bird("green", "two")
    xique.call("gezhi")





def test_02():

    # 实例化类
    x = MyClass()

    # 访问类的属性和方法
    print("MyClass 类的属性 i 为：", x.i)
    print("MyClass 类的方法 f 输出为：", x.f())





if __name__ == '__main__':
    # test()

    test_02()