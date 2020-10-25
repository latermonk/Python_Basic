


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




if __name__ == '__main__':
    test()