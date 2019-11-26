# coding=utf-8

import glob
import json

from delete.spc import *
from extract.lang import *
from replace.fj import *
from replace.qb import *

S_LIMIT = int(5e6)
WINDOW_WIDTH = 7


def read_and_write1(file_name):
    with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'r', encoding='utf-8') as fo:
        sentence_list = fo.readlines()
    index = len(glob.glob(pathname='D:\\nlp dataset\\lm pre-train corpus\\clean data\\*.txt')) - 1
    with open(file_name, 'r', encoding='utf-8') as file_object:
        # 需要修改部分
        for line in file_object:
            temp = json.loads(line)['chinese'].split('。')
            for s in temp:
                if s != '':
                    sentence_list.append(s + '。\n')

            if len(sentence_list) >= S_LIMIT:
                with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\' + str(index) + '.txt', 'w',
                          encoding='utf-8') as fo:
                    fo.writelines(sentence_list[:S_LIMIT])
                sentence_list = sentence_list[S_LIMIT:]
                index += 1
    with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'w', encoding='utf-8') as fo:
        fo.writelines(sentence_list)


def read_and_write2(file_path):
    file_list = os.listdir(file_path)
    for i in range(0, len(file_list)):
        path = os.path.join(file_path, file_list[i])
        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as file_object:
                # 需要修改部分
                for line in file_object:
                    temp = json.loads(line)['content'].split('。')
                    for s in temp:
                        if s != '':
                            sentence_list.append(s + '。\n')

                    if len(sentence_list) >= S_LIMIT:
                        with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\' + str(index[0]) + '.txt', 'w',
                                  encoding='utf-8') as fo:
                            fo.writelines(sentence_list[:S_LIMIT])
                        sentence_list[:] = sentence_list[S_LIMIT:]
                        index[0] += 1
        else:
            read_and_write2(path)


def clean_and_rewrite(file_name):
    sentence_list = []
    with open(file_name, 'r', encoding='utf-8') as fo:
        for line in fo:
            if len(line.replace('\n', '').replace('。', '').replace('，', '')) >= WINDOW_WIDTH:
                sentence_list.append(delete_sp_char(q2b(f2j(line))))

    with open(file_name, 'w', encoding='utf-8') as fo:
        for sentence in sentence_list:
            fo.write(sentence)


# <editor-fold desc="原始数据读取">
# with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'r', encoding='utf-8') as fo:
# 	sentence_list = fo.readlines()
# index = [len(glob.glob(pathname='D:\\nlp dataset\\lm pre-train corpus\\clean data\\*.txt'))-1]
# read_and_write2('D:\\nlp dataset\\lm pre-train corpus\\noisy data\\webtext2019zh')
# with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'w', encoding='utf-8') as fo:
# 	fo.writelines(sentence_list)
# </editor-fold>

# <editor-fold desc="数据预处理">
# clean_and_rewrite('D:\\nlp dataset\\lm pre-train corpus\\clean data\\2.txt')
for i in range(20):
    clean_and_rewrite('D:\\nlp dataset\\lm pre-train corpus\\clean data\\' + str(i) + '.txt')
# </editor-fold>

# <editor-fold desc="语料提取">
char_dict = {}
extract_char_lang(char_dict, 'D:\\nlp dataset\\lm pre-train corpus\\clean data\\')
# </editor-fold>
