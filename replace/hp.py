# coding=utf-8

import jieba
import pypinyin


def h2p(word):
    """
    汉语到拼音转换
    :param word:
    :return:
    """
    word = ' '.join(jieba.cut(word))
    s = ''
    for i in pypinyin.pinyin(word):
        s += ''.join(i) + " "
    s_list = s.split(' ')
    i = 0
    while i < len(s_list):
        if s_list[i] == '':
            s_list.pop(i)
        else:
            i += 1
    s = ' '.join(s_list)

    return s
