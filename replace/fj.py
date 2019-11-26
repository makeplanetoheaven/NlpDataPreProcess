# coding=utf-8


from openccpy.opencc import *


def f2j(ustring):
    """
    繁体转简体
    :param ustring:
    :return:
    """
    rstring = Opencc.to_simple(ustring)

    return rstring


def j2f(ustring):
    """
    简体转繁体
    :param ustring:
    :return:
    """
    rstring = Opencc.to_traditional(ustring)

    return rstring
