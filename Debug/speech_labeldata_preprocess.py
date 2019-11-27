# coding=utf-8

import os
import json
from replace import hp


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


# <editor-fold desc="原始标签数据读取即转换">
# source_file_path = 'C:\\Users\\hasee\\Desktop\\labelset'
# target_file_path = 'C:\\Users\\hasee\\Desktop\\new_labelset'
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
label_file_path = 'C:\\Users\hasee\Desktop\labelset'
target_dict_file = './pinyin_dict.json'
read_and_write3(label_file_path, target_dict_file)
# </editor-fold>
