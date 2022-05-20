from nonebot.adapters.onebot.v11 import Message
import re

# 网上抄了一个处理图片的函数
# 利用正则匹配所有信息中的图片信息并去除url
async def remove_image_num(msg):
    pattern = re.compile('\[CQ:image,file=(\w|\d)*\.image,url=https://gchat.qpic.cn/(\w|\d|\/|-|_|\?|=|,)*\]')
    result = pattern.sub(lambda match : match.group().split(',url=')[0] + r"]}", msg)
    # 防止操作系统换行符不同导致的问题
    return result.replace('\r\n', '\n')

async def repeat_whisper(user_id : int, times : int) -> Message:
    '''user_id : 用户的QQ号 times : 已经复读的次数'''
    return Message(f' [CQ:at,qq={user_id}] 终结了长达{times}次的复读, 为人类文明的进步迈出了一小步!')

async def repeat_interrupt(user_id) -> Message:
    '''user_id : 用户的QQ号'''
    return Message(f'有复读人! 打断,并打断 [CQ:at,qq={user_id}] 的腿杀鸡儆猴!')