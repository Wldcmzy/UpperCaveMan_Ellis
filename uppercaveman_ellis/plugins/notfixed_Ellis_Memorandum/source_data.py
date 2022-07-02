from ..global_args import Memorandum_data_path
from nonebot.log import logger
import os

SAVE_DATA_SEP = '\n'

def form_file_name(group_id : str) -> str:
    '''返回群号指定文件的路径'''
    return Memorandum_data_path + group_id + '.txt'

def file_write(group_id : str, text : str) -> str:
    '''群号and要写入的内容'''
    if not text: return '你这话说的好像说了话一样'
    file_name = form_file_name(group_id)
    if not os.path.exists(Memorandum_data_path):
        os.makedirs(Memorandum_data_path)
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(text + SAVE_DATA_SEP)
    return f'大概写好了,内容为:\n{text}'

def file_read(group_id : str) -> str:
    '''输入要查询备忘录的群号'''
    file_name, ret = form_file_name(group_id), ''
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            lst = f.read().strip().split(SAVE_DATA_SEP)
        if lst[0]:
            for i, each in enumerate(lst):
                ret += f'{i + 1}: {each}\n'
    if not ret: ret = '无'
    return '备忘录:\n' + ret 

def file_delete(group_id : str, index : str) -> str:
    '''index : 要产出的条目编号(但须要更够强制转换成int)'''
    file_name = form_file_name(group_id)
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            lst = f.read().strip().split(SAVE_DATA_SEP)
        text = lst[int(index) - 1]
        del lst[int(index) - 1]
    except Exception as e:
        return '呜呜呜,出错了~\n' + str(e)
    with open(file_name, 'w', encoding='utf-8') as f:
        for each in lst:
            f.write(each + SAVE_DATA_SEP)
    return f'大概删了,删除内容为:\n{text}'
