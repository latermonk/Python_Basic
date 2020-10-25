# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def list_test():
    list = ['runoob', 786, 2.23, 'john', 70.2]
    tinylist = [123, 'john']

    print(list)
    print(tinylist)


def number_test():
    a = 100
    # b = 0122l
    c = -32.54e100
    d = 9.322e-36j

    print(a)
    # print(b)
    print(c)
    print(d)


def string_test():
    s = 'abcdef'
    print(s[1:8])


def string_test_more():
    str = 'Hello World!'

    print (str)  # 输出完整字符串
    print(str[0])  # 输出字符串中的第一个字符
    print(str[2:5] ) # 输出字符串中第三个至第六个之间的字符串
    print(str[2:] ) # 输出从第三个字符开始的字符串
    print(str * 2) # 输出字符串两次
    print(str + "TEST")  # 输出连接的字符串


def list_test_more():
    print("list_test_more")

    name_list = ['sean', 'tom', 'jack', 'Angelia', 'Daisy', 'jack']
    print(name_list)

    name_list.append('david')
    print(name_list)

    print(name_list.count('david'))
    print(name_list.count('jack'))

    # name_list.extend('Hello,My name is sean')
    # print(name_list)

    name_list.insert(2, 'Adam')
    print(name_list)

    # name_list.pop()
    # print(name_list)
    # name_list.pop()
    # print(name_list)
    # name_list.pop()
    # print(name_list)
    # name_list.pop()
    # print(name_list)
    # name_list.pop()
    # print(name_list)

    count = 0
    while (count < 3):
        # name_list.pop()
        print(name_list)
        break

    fruits = ['banana', 'apple', 'mango']
    for fruit in fruits:  # 第二个实例
        print('当前水果 :', fruit)


def dict_test():
    dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])


    dict['Age'] = 8  # 更新
    dict['School'] = "RUNOOB"  # 添加
    print("dict['Name']: ", dict['Name'])
    print("dict['Age']: ", dict['Age'])







def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

    # list_test()

    # number_test()


    # string_test()


    # string_test_more()

    # list_test_more()

    dict_test()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
