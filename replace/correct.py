# coding=utf-8

import pycorrector


def e2r(word):
    """
    汉字纠错
    :param word:
    :return:
    """
    corrected_sent, detail = pycorrector.correct(word)

    return corrected_sent, detail
