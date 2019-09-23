# coding=utf-8


def delete_sp_char (ustring: str):
	# <editor-fold desc="特殊字符替换">
	restring = ustring.replace('&nbsp', '')\
		.replace('　', '')\
		.replace('■', '')\
		.replace('●', '')\
		.replace('▼', '')\
		.replace('▽', '')\
		.replace('▲', '')\
		.replace('▎', '')\
		.replace('▍', '')\
		.replace('▌', '')\
		.replace('▊', '')\
		.replace('↑', '')\
		.replace('↓', '')\
		.replace('←', '')\
		.replace('↙', '')\
		.replace('↖', '')\
		.replace('↗', '')\
		.replace('★', '')\
		.replace('☆', '')\
		.replace('◆', '')\
		.replace('🍀', '')\
		.replace('🐕', '')\
		.replace('🐱', '')\
		.replace('◎', '')\
		.replace('©', '')\
		.replace('○', '')\
		.replace('丶', '')\
		.replace('~*', '')\
		.replace('━', '')\
	# </editor-fold>

	# <editor-fold desc="重复字符替换">
	restring = restring.replace('~~', '')\
		.replace('，，', '')\
		.replace(',,', ',')\
		.replace('""', '') \
		.replace('。。', '。') \
		.replace('-----', '')\
		.replace('_____', '')\
		.replace('………', '')\
		.replace('>>>', '')\
		.replace('....', '')\
		.replace('——', '—')\
		.replace('***', '')\
		.replace('===', '')\
		.replace('？。', '？') \
		.replace('！。', '！') \
		.replace('！！！！', '！') \
		# </editor-fold>

	# <editor-fold desc="出现位置错误字符替换">
	restring = restring.lstrip('”')\
		.lstrip('?')\
		.lstrip('】')\
		.lstrip(')')\
		.lstrip('）')\
		.lstrip('-')\
		.lstrip('—')\
		.lstrip('，')\
		.lstrip('…')\
		.lstrip('：')\
		.lstrip('；')\
		.lstrip('·')\
		.lstrip('」')\
		.lstrip('》')\
		.lstrip('*')\
		.lstrip('.')\
		.lstrip('=')\
		.lstrip('~')\
		.lstrip('\'')\
		.lstrip('丨')\
		.lstrip('！')
	# </editor-fold>

	# <editor-fold desc="无效字符替换">
	restring = restring.replace('（）', '')
	restring = restring.replace('（，）', '')
	# </editor-fold>

	return restring
