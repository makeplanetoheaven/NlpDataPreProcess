# coding=utf-8

import json
import os
import re

from replace import hp
from replace.digitaltrans import *
from replace.fj import *
from replace.qb import *


def read_and_write(source_file_path, target_file_path):
    file_list = os.listdir(source_file_path)
    for file in file_list:
        source_file = os.path.join(source_file_path, file)
        target_file = os.path.join(target_file_path, file)

        content_list = []
        with open(source_file, 'r', encoding='utf-8') as fo:
            for line in fo:
                data_path, _, hanzi = line.rstrip('\n').split('\t')
                pinyin = hp.h2p(hanzi)
                content_list.append(data_path + '\t' + pinyin + '\t' + hanzi + '\n')
        with open(target_file, 'w', encoding='utf-8') as fo:
            fo.writelines(content_list)


def read_and_write2(TRANS_file_path, scp_file_path, target_label_file, data_file_name):
    # 1.读取音频ID到汉字的文件
    id2hanzi_dict = {}
    with open(TRANS_file_path, 'r', encoding='utf-8') as fo:
        index = 0
        for line in fo:
            if index > 0:
                utterance_id, _, hanzi = line.rstrip('\n').split('\t')
                id2hanzi_dict[utterance_id] = hanzi

            index += 1

    # 2.根据ID到路径的文件，生成标注数据
    label_list = []
    with open(scp_file_path, 'r', encoding='utf-8') as fo:
        for line in fo:
            utterance_id, wav_path = line.rstrip('\n').split('\t')
            data_path = data_file_name + '/' + wav_path
            hanzi = id2hanzi_dict[utterance_id]
            pinyin = hp.h2p(hanzi)
            label_list.append(data_path + '\t' + pinyin + '\t' + hanzi + '\n')

    # 3.存储标注数据
    with open(target_label_file, 'w', encoding='utf-8') as fo:
        fo.writelines(label_list)


def read_and_write3(label_file_path, pinyin_dict_file):
    # 1.拼音字典统计
    file_list = os.listdir(label_file_path)
    pinyin_dict = {}
    for file in file_list:
        label_file = os.path.join(label_file_path, file)
        with open(label_file, 'r', encoding='utf-8') as fo:
            for line in fo:
                _, pinyin, _ = line.rstrip('\n').split('\t')
                pinyin_list = pinyin.split(' ')
                for c in pinyin_list:
                    pinyin_dict[c] = 1

    # 2.拼音字典存储
    index = 0
    for key in pinyin_dict:
        pinyin_dict[key] = index
        index += 1
    with open(pinyin_dict_file, 'w', encoding='utf-8') as fo:
        json.dump(pinyin_dict, fo, ensure_ascii=False, indent=2)


def read_and_write4(label_file_path):
    Punctuation = "·!！？?:\\\\｡。\"＂\-＃＄％\\%＆＇()（）＊＋，,－／/：;；＜＝＞＠［＼］\\[\\]＾＿｀`｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."

    # 1.字符去除
    file_list = os.listdir(label_file_path)
    for file in file_list:
        label_file = os.path.join(label_file_path, file)
        print('processing', label_file)
        content_list = []
        with open(label_file, 'r', encoding='utf-8') as fo:
            for line in fo:
                data_path, pinyin, hanzi = line.rstrip('\n').split('\t')
                hanzi = hanzi.replace('[FIL]', '').replace('[SPK]', '').replace('[FIL', '').replace('FIL]', '') \
                    .replace(' ', '').replace('\u0017', '').replace('\u0014', '').replace('\ufeff', '')
                res = re.findall('[a-zA-Z]+', hanzi)
                if len(res) < 1:
                    hanzi = re.sub("[%s]+" % Punctuation, "", dig2chinese2(q2b(f2j(hanzi))))
                    content_list.append(data_path + '\t' + pinyin + '\t' + hanzi + '\n')
        with open(label_file, 'w', encoding='utf-8') as fo:
            fo.writelines(content_list)


def read_and_write5(label_file_path, pinyin2char_dict):
    file_list = os.listdir(label_file_path)
    for file in file_list:
        label_file = os.path.join(label_file_path, file)
        with open(label_file, 'r', encoding='utf-8') as fo:
            for line in fo:
                data_path, pinyin, hanzi = line.rstrip('\n').split('\t')
                pinyin_list = pinyin.split(' ')
                for i in range(len(pinyin_list)):
                    if pinyin_list[i] in pinyin2char_dict:
                        pinyin2char_dict[pinyin_list[i]][hanzi[i]] = 1
                    else:
                        pinyin2char_dict[pinyin_list[i]] = {hanzi[i]: 1}


def read_and_write6(label_file_path, n_gram):
    file_list = os.listdir(label_file_path)
    n_gram_freq_dict = {}
    for file in file_list:
        label_file = os.path.join(label_file_path, file)
        with open(label_file, 'r', encoding='utf-8') as fo:
            for line in fo:
                data_path, pinyin, hanzi = line.rstrip('\n').split('\t')

                # 滑动提取
                content_list = pinyin.split(' ')
                n_content = len(content_list)
                for i in range(n_content - n_gram + 1):
                    gram = ' '.join(content_list[i:i + n_gram])
                    if gram in n_gram_freq_dict:
                        n_gram_freq_dict[gram] += 1
                    else:
                        n_gram_freq_dict[gram] = 1

    return n_gram_freq_dict


# <editor-fold desc="原始标签数据读取及转换">
# source_file_path = 'E:\\Jarvis项目\code\\NlpDataPreProcess\Debug\labelset'
# target_file_path = 'E:\\Jarvis项目\code\\NlpDataPreProcess\Debug\\new_labelset'
# read_and_write(source_file_path, target_file_path)
# </editor-fold>

# <editor-fold desc="新音频数据标签整理">
# train_TRANS_file_path = 'C:\\Users\\hasee\Desktop\MAGICDATA_Mandarin_Chinese_Speech\MAGICDATA_Mandarin_Chinese_Speech\TRANS.txt'
# dev_TRANS_file_path = 'C:\\Users\\hasee\Desktop\MAGICDATA_Mandarin_Chinese_Speech\MAGICDATA_Mandarin_Chinese_Speech\TRANS_dev_corrected.txt'
# train_scp_file_path = 'C:\\Users\\hasee\Desktop\MAGICDATA_Mandarin_Chinese_Speech\MAGICDATA_Mandarin_Chinese_Speech\\train.scp'
# dev_scp_file_path = 'C:\\Users\\hasee\Desktop\MAGICDATA_Mandarin_Chinese_Speech\MAGICDATA_Mandarin_Chinese_Speech\\dev.scp'
# test_scp_file_path = 'C:\\Users\\hasee\Desktop\MAGICDATA_Mandarin_Chinese_Speech\MAGICDATA_Mandarin_Chinese_Speech\\test.scp'
# target_label_file = 'C:\\Users\hasee\Desktop\labelset'
#
# read_and_write2(dev_TRANS_file_path, dev_scp_file_path, target_label_file + '\magicdata_dev.txt',
#                 'MAGICDATA_Mandarin_Chinese_Speech')
# </editor-fold>

# <editor-fold desc="拼音字典统计">
# label_file_path = 'E:\\Jarvis项目\code\\NlpDataPreProcess\Debug\labelset'
# target_dict_file = './pinyin_dict.json'
# read_and_write3(label_file_path, target_dict_file)
# </editor-fold>

# <editor-fold desc="去除标签集中的标点符号，特殊符号，英文">
# label_file_path = 'E:\\Jarvis项目\code\\NlpDataPreProcess\Debug\labelset'
# read_and_write4(label_file_path)
# </editor-fold>

# <editor-fold desc="根据标签数据得到pinyin2char_dict">
# label_file_path = 'C:\\Users\Dell\Desktop\labelset'
# pinyin2char_dict = {}
# read_and_write5(label_file_path, pinyin2char_dict)
# pinyin_list = sorted(list(pinyin2char_dict.keys()))
# new_pinyin2char_dict = {}
# for pinyin in pinyin_list:
#     new_pinyin2char_dict[pinyin] = ''.join(sorted(list(pinyin2char_dict[pinyin].keys())))
# with open('./pinyin2char_dict.json', 'w', encoding='utf-8') as fo:
#     json.dump(new_pinyin2char_dict, fo, ensure_ascii=False, indent=2)
# </editor-fold>

# <editor-fold desc="根据标签数据得到n_gram_freq">
label_file_path = 'C:\\Users\Dell\Desktop\labelset'
freq_file_path = 'C:\\Users\Dell\Desktop\\binary_freq.txt'
n_gram_freq_dict = read_and_write6(label_file_path, 2)
with open(freq_file_path, 'r', encoding='utf-8') as fo:
    for line in fo:
        gram, freq = line.rstrip('\n').split('\t')
        if gram in n_gram_freq_dict:
            n_gram_freq_dict[gram] += int(freq)
        else:
            n_gram_freq_dict[gram] = int(freq)
n_gram_freq_list = []
for key in n_gram_freq_dict:
    n_gram_freq_list.append([key, n_gram_freq_dict[key]])
n_gram_freq_list = sorted(n_gram_freq_list, key=lambda ele: ele[1], reverse=True)
with open(freq_file_path, 'w', encoding='utf-8') as fo:
    for gram, freq in n_gram_freq_list:
        fo.write(gram + '\t' + str(freq) + '\n')
# </editor-fold>
