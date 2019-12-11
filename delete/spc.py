# coding=utf-8


def delete_sp_char(ustring: str, is_space=False):
    # <editor-fold desc="去除空格(会把换行也去除)">
    if is_space:
        ustring = ''.join(ustring.split())
    # </editor-fold>

    # <editor-fold desc="特殊字符替换">
    restring = delete_emoji_char(ustring)
    restring = restring.replace('&nbsp', '') \
        .replace('<br>', '') \
        .replace('\u001f', '') \
        .replace('\u0000', '') \
        .replace('\u0018', '') \
        .replace('\u0014', '') \
        .replace('\t', '') \
        .replace('􊥭', '') \
        .replace('􀀁', '') \
        .replace('●', '') \
        .replace('▼', '') \
        .replace('▽', '') \
        .replace('▲', '') \
        .replace('▎', '') \
        .replace('▍', '') \
        .replace('▌', '') \
        .replace('▊', '') \
        .replace('■', '') \
        .replace('▇', '') \
        .replace('▆', '') \
        .replace('↑', '') \
        .replace('↓', '') \
        .replace('←', '') \
        .replace('↙', '') \
        .replace('↖', '') \
        .replace('↗', '') \
        .replace('★', '') \
        .replace('☆', '') \
        .replace('◆', '') \
        .replace('◎', '') \
        .replace('©', '') \
        .replace('○', '') \
        .replace('※', '') \
        .replace('丶', '') \
        .replace('~*', '') \
        .replace('━', '') \
        # </editor-fold>

    # <editor-fold desc="重复字符替换">
    restring = restring.replace('~~', '') \
        .replace('，，', '') \
        .replace(',,', ',') \
        .replace('""', '') \
        .replace('。。', '。') \
        .replace('-----', '') \
        .replace('_____', '') \
        .replace('………', '') \
        .replace('>>>', '') \
        .replace('....', '') \
        .replace('——', '—') \
        .replace('***', '') \
        .replace('===', '') \
        .replace('？。', '？') \
        .replace('！。', '！') \
        .replace('！！！！', '！') \
        # </editor-fold>

    #  <editor-fold desc="出现位置错误字符替换">
    restring = restring.lstrip('”') \
        .lstrip('?') \
        .lstrip('】') \
        .lstrip(')') \
        .lstrip('）') \
        .lstrip('-') \
        .lstrip('—') \
        .lstrip('，') \
        .lstrip('…') \
        .lstrip('：') \
        .lstrip('；') \
        .lstrip('·') \
        .lstrip('」') \
        .lstrip('》') \
        .lstrip('*') \
        .lstrip('.') \
        .lstrip('=') \
        .lstrip('~') \
        .lstrip('\'') \
        .lstrip('丨') \
        .lstrip('！')
    # </editor-fold>

    # <editor-fold desc="无效字符替换">
    restring = restring.replace('（）', '') \
        .replace('（，）', '') \
        .replace('()', '') \
        .replace('(;)', '') \
        .replace('(,)', '') \
        .replace('“”', '')
    # </editor-fold>

    return restring


def delete_emoji_char(ustring):
    """去除表情符号"""
    return str(bytes(ustring, encoding='utf-8').decode('utf-8').encode('gbk', 'ignore').decode('gbk'))
