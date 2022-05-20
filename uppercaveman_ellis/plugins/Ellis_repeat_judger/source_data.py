from nonebot.adapters.onebot.v11 import Message

async def repeat_whisper(user_id : int, times : int) -> Message:
    '''user_id : 用户的QQ号 times : 已经复读的次数'''
    return Message(f' [CQ:at,qq={user_id}] 终结了长达{times}次的复读, 为人类文明的进步迈出了一小步!')

async def repeat_interrupt(user_id) -> Message:
    '''user_id : 用户的QQ号'''
    return Message(f'有复读人! 打断,并打断 [CQ:at,qq={user_id}] 的腿杀鸡儆猴!')