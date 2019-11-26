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
    print(word)
    s = ''
    for i in pypinyin.pinyin(word):
        s += ''.join(i) + " "

    return s
