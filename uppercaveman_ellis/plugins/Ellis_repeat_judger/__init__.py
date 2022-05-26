from nonebot import on_message
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.permission import SUPERUSER
from nonebot.log import logger
from .privilege import Role_RepeatJudger
from .source_data import repeat_interrupt, repeat_whisper, remove_image_num
from ..global_args import Repeat_judger_args_dic, PRIORITY_PASSIVE

E_messsage = {}
E_repeat_judger = on_message(
    rule=Role_RepeatJudger,
    priority=PRIORITY_PASSIVE
)

@E_repeat_judger.handle()
async def repeat_judger(event : Event) -> None:
    #获取基本信息
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    msg = await remove_image_num(msg)
    # 若消息集合中没有这个群的信息, 新建一个
    if group_id not in E_messsage: 
        E_messsage[group_id] = {'text' : msg, 'times' : 0}
    
    # 若信息变换, 重置消息集合中对应的内容
    if E_messsage[group_id]['text'] != msg:
        # 若此群符合发送wisper陈述条件,且信息变换时此群已经在复读, 发送wisper内容
        if group_id not in  Repeat_judger_args_dic['interrupt_group'] and group_id in Repeat_judger_args_dic['whisper_group']:
            if E_messsage[group_id]['times'] >= Repeat_judger_args_dic['threshold']:
                relpy_text = await repeat_whisper(user_id, E_messsage[group_id]['times'])
                await E_repeat_judger.send(relpy_text)
        E_messsage[group_id] = {'text' : msg, 'times' : 0}

    E_messsage[group_id]['times'] += 1

    # 若此群在interrupt集合中并被判定为复读, 发送interrupt内容打断复读 
    if group_id in Repeat_judger_args_dic['interrupt_group']:
        if E_messsage[group_id]['times'] >= Repeat_judger_args_dic['threshold']:
            reply_text = await repeat_interrupt(user_id)
            await E_repeat_judger.send(reply_text)
            E_messsage[group_id]['times'] -= Repeat_judger_args_dic['threshold']
        
    