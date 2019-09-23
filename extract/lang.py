# coding=utf-8

import os


def extract_char_lang(char_dict, file_path):
	file_list = os.listdir(file_path)
	for file in file_list:
		path = os.path.join(file_path, file)
		if os.path.isfile(path):
			with open(path, 'r', encoding='utf-8') as file_object:
				for line in file_object:
					for c in line:
						char_dict[c] = 1
		else:
			extract_char_lang(char_dict, path)