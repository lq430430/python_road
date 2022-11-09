# coding=utf-8
"""统计一句话，有几个字母a，有几个单词glory"""


def string_contain(s, a, b):
    a_num = 0
    for i in s:
        if i == 'str':
            a_num += 1
        else:
            pass
    print(a + "的个数是：", a_num)
    print(b + "的个数是：", s.count(b))


"""一句话里删除所有的a """


def string_del(s, a):




"""判断一个字符串中的括号是否成对出现："""


def count_list(str):
    list1 = list(str)
    dict = {}
    for element in list1:
        if dict.get(element) == None:
            dict[element] = 1
        else:
            dict[element] += 1

    if dict.get('(') != dict.get(')'):
        return print("括号未成对出现")
    elif dict.get('[') != dict.get(']'):
        return print("中括号未成对出现")
    elif dict.get('{') != dict.get('}'):
        return print("花括号未成对出现")
    else:
        return print("字符串中各特殊符号成对出现")


if __name__ == '__main__':
    str1 = "(abc[]{li}))"
    count_list(str1)
    string1 = "a boy,a girl,you are my boy"
    str2 = "a"
    str3 = "boy"

    string_contain(string1, str2, str3)
