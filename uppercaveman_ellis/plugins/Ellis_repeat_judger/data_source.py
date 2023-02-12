from nonebot.adapters.onebot.v11 import Message
from random import randint
import re
import time
import hashlib


async def remove_image_num(msg):
    '''利用正则匹配所有信息中的图片信息并去除多余信息'''
    pattern = re.compile('\[CQ:image,file=(\w|\d)*\.image,(.+?)url=https://gchat.qpic.cn/(\w|\d|\/|-|_|\?|=|,)*\]')
    result = pattern.sub(lambda match : match.group().split(',url=')[0] + r"]}", msg)
    # 防止操作系统换行符不同导致的问题
    return result.replace('\r\n', '\n')

async def repeat_whisper(user_id : str, times : int) -> Message:
    '''
    复读结束回复语句
    user_id : 用户的QQ号 
    times : 已经复读的次数
    '''
    return Message(f' [CQ:at,qq={user_id}] 终结了长达{times}次的复读, 为人类文明的进步迈出了一小步!')

async def repeat_interrupt(user_id:str, user_level: int = 0) -> Message:
    '''
    复读打断语句
    user_id : 用户的QQ号
    user_level : 0 普通群友 , 1 群主 , 2  管理员, -1 超级用户
    '''
    base_str = f'有复读人! 打断,并打断 [CQ:at,qq={user_id}] '
    tail_str = '的腿杀鸡儆猴!'
    rand_code = '\nCode:' + hashlib.md5(str(time.time()).encode('utf-8')).hexdigest()[ : 6]
    if user_level == -1: tail_str = '......\n 哦那没事了, 您想干嘛就干嘛 [CQ:face,id=107] '
    elif user_level == 1: tail_str = '......\n 哦是群主啊, 那没事了...'
    elif user_level == 2: tail_str = '......\n 哦是管理员啊, 那没事了...'
    return Message(base_str + tail_str + rand_code)