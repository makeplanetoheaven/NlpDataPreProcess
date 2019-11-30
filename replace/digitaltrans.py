# coding=utf-8


def dig2chinese1(dig_str: str) -> str:
    """
    阿拉伯数字和中文数字互相转换(有个十百千)
    :param dig_str:
    :return:
    """
    a = int(dig_str)
    b = len(dig_str)  # 字符串位数
    number = ['零', '一', '二', '三', '四', '五', '六', '七', '八', '九']
    unit = ['零', '十', '百', '千', '万', '亿']
    dig_list = []  # 储存中文数字串
    while (b > 0):
        c = a // pow(10, b - 1)
        if (c != 0):
            dig_list.append(number[c])
        if (c == 0 and len(dig_list) > 1 and dig_list[-1] != unit[0]):
            dig_list.append(number[c])
        d = a % pow(10, b - 1)
        e = (b - 1) % 4
        if (e > 0 and c != 0):
            dig_list.append(unit[e])
        f = b // 4
        if (f == 1 and e == 0 and dig_list[-1] != unit[5]):
            dig_list.append(unit[4])
        elif (f == 2 and e == 0):
            dig_list.append(unit[5])
        a = d
        b = b - 1
    i = 0
    res = ''
    while (i < len(dig_list)):
        if (i == 0):
            if (dig_list[i] == number[1] and dig_list[i + 1] == unit[1]):
                res += dig_list[i + 1]
                i = i + 2
        if (i != len(dig_list) - 1 and dig_list[i] == unit[0] and (
                                dig_list[i - 1] == unit[1] or dig_list[i - 1] == unit[2] or dig_list[i - 1] == unit[
                        3] or dig_list[i - 1] ==
                    unit[4]) and (dig_list[i + 1] == unit[4] or dig_list[i + 1] == unit[5])):
            res += dig_list[i + 1]
            i = i + 2
        if (i == len(dig_list) - 1 and dig_list[i] == unit[0]):
            break
        else:
            res += dig_list[i]
            i = i + 1

    return res


def dig2chinese2(dig_str: str) -> str:
    """
    阿拉伯数字和中文数字互相转换(无个十百千)
    :param dig_str:
    :return:
    """
    dict1 = {'0': '零', '1': '一', '2': '二', '3': '三', '4': '四', '5': '五', '6': '六', '7': '七', '8': '八', '9': '九'}
    zifuchuang1 = list(dig_str)
    zifuchuang2 = []
    for i in zifuchuang1:
        is_dig = False
        for key, val in dict1.items():
            if key == i:
                zifuchuang2.append(val)
                is_dig = True
                break
        if not is_dig:
            zifuchuang2.append(i)

    return "".join(zifuchuang2)
