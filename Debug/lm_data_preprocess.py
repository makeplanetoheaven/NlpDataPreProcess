# coding=utf-8

import glob
import json

from delete.spc import *
from extract.lang import *
from replace.fj import *
from replace.qb import *
from usual_re import *

S_LIMIT = int(5e6)
WINDOW_WIDTH = 32


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


def clean_and_rewrite1(file_name):
    sentence_list = []
    with open(file_name, 'r', encoding='utf-8') as fo:
        for line in fo:
            if len(line.replace('\n', '').replace('。', '').replace('，', '')) >= WINDOW_WIDTH:
                if PATTERN_CH.search(line):  # 去除不包含中文的句子
                    sentence_list.append(temp_delete_char(delete_sp_char(q2b(f2j(line)))))

    with open(file_name, 'w', encoding='utf-8') as fo:
        for sentence in sentence_list:
            fo.write(sentence)


def clean_and_rewrite2(file_path):
    file_list = os.listdir(file_path)
    for i in range(0, len(file_list)):
        file_name = os.path.join(file_path, file_list[i])
        sentence_list = []
        with open(file_name, 'r', encoding='utf-8') as fo:
            for line in fo:
                sentence_list.append(temp_delete_char(delete_sp_char(q2b(f2j(line)))).replace(' ', ',').replace('\x7f', ''))
        with open(file_name, 'w', encoding='utf-8') as fo:
            for sentence in sentence_list:
                if len(sentence.replace('\n', '')) > 4:
                    fo.write(sentence)


def temp_delete_char(ustring):
    restring = ustring.replace('\u0000', '')\
        .replace('\u0001', '')\
        .replace('\u0002', '')\
        .replace('\u0003', '')\
        .replace('\u0004', '')\
        .replace('\u0005', '')\
        .replace('\u0006', '')\
        .replace('\u0007', '')\
        .replace('\u000e', '')\
        .replace('\u000f', '')\
        .replace('\u0010', '')\
        .replace('\u0011', '')\
        .replace('\u0012', '')\
        .replace('\u0013', '')\
        .replace('\u0014', '')\
        .replace('\u0015', '')\
        .replace('\u0016', '')\
        .replace('\u0017', '')\
        .replace('\u0018', '')\
        .replace('\u0019', '')\
        .replace('\u001a', '')\
        .replace('\u001b', '')\
        .replace('\b', '')

    return restring


# <editor-fold desc="原始数据读取">
# with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'r', encoding='utf-8') as fo:
# 	sentence_list = fo.readlines()
# index = [len(glob.glob(pathname='D:\\nlp dataset\\lm pre-train corpus\\clean data\\*.txt'))-1]
# read_and_write2('D:\\nlp dataset\\lm pre-train corpus\\noisy data\\webtext2019zh')
# with open('D:\\nlp dataset\\lm pre-train corpus\\clean data\\left.txt', 'w', encoding='utf-8') as fo:
# 	fo.writelines(sentence_list)
# </editor-fold>

# <editor-fold desc="数据预处理">
# source_file_path = 'D:\项目\Jarvis\Core\lm_data\\'
# file_list = os.listdir(source_file_path)
# for file_name in file_list:
#     file_path = os.path.join(source_file_path, file_name)
#     txt_file_list = os.listdir(file_path)
#     for txt_file_name in txt_file_list:
#         txt_file_path = os.path.join(file_path, txt_file_name)
#         clean_and_rewrite1(txt_file_path)
# </editor-fold>

# <editor-fold desc="语料提取">
# char_dict = {}
# extract_char_lang(char_dict, 'D:\项目\Jarvis\Core\lm_data\\')
# char_list = sorted(list(char_dict.keys()))
# new_char_dict = {}
# for i, char in enumerate(char_list):
#     new_char_dict[char] = i
# with open('./char_dict.json', 'w', encoding='utf-8') as fo:
#     json.dump(new_char_dict, fo, ensure_ascii=False, indent=2)
# </editor-fold>

# <editor-fold desc="除语言模型外其他模型训练数据处理">
file_path = 'D:\\项目\\Jarvis\\Core\\news\\'
clean_and_rewrite2(file_path)
# </editor-fold>
