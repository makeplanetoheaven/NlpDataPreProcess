# coding=utf-8

import os

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


source_file_path = 'C:\\Users\\hasee\\Desktop\\labelset'
target_file_path = 'C:\\Users\\hasee\\Desktop\\new_labelset'
read_and_write(source_file_path, target_file_path)
