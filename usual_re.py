# coding=utf-8

import re

# pattern
PATTERN_CH = re.compile(u'[\u4e00-\u9fa5]')  # 检查中文

# char
PUNCTUATION = "[%s]+" % "·!！？?:\\\\｡。\"＂\-＃＄％\\%＆＇()（）＊＋，,－／/：;；＜＝＞＠［＼］\\[\\]＾＿｀`｛｜｝～｟｠｢｣､、〃《》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏."
SP_CHAR = '[^\w\u4e00-\u9fff]+'  # 过滤非中英文字符
