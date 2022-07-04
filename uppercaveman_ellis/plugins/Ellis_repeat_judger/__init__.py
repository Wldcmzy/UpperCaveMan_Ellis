from tokenize import group
import nonebot
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Event, GROUP, GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
from random import randint
from .data_source import repeat_interrupt, repeat_whisper, remove_image_num
from .config import Config
from nonebot.log import logger

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

Whisper_group = plugin_config.repeat_judger_group
Interrupt_group = plugin_config.repeat_judger_group_interrupt
Repeat_threshold = plugin_config.repeat_judger_threshold
Repeat_threshold_random_add = plugin_config.repeat_judge_threshold_random_add

Group_Messsage = {}

repeat_judger = on_message(permission=GROUP, priority=90)

@repeat_judger.handle()
async def _(event : Event) -> None:
    #获取基本信息
    useless, group_id, user_id = event.get_session_id().split('_')
    msg = await remove_image_num(str(event.get_message()))
    logger.debug(f'<<<<<<<<<<<<<<<<<<<<<{event.get_message()}')
    logger.debug(f'>>>>>>>>>>>>>>>>>>>{msg}')

    # 若消息集合中没有这个群的信息, 新建一个
    if group_id not in Group_Messsage: 
        Group_Messsage[group_id] = {'text' : msg, 'times' : 0}
    
    # 若信息变换, 按照条件执行操作, 并重置消息集合中对应的内容
    if Group_Messsage[group_id]['text'] != msg:
        # 若此群符合发送wisper消息条件,且信息变换时此群已经在复读, 发送wisper内容
        if group_id not in Interrupt_group and group_id in Whisper_group:
            if Group_Messsage[group_id]['times'] >= Repeat_threshold:
                relpy_text = await repeat_whisper(user_id, Group_Messsage[group_id]['times'])
                await repeat_judger.send(relpy_text)

        Group_Messsage[group_id] = {'text' : msg, 'times' : 0}


    Group_Messsage[group_id]['times'] += 1

    # 若此群在interrupt集合中并被判定为复读, 发送interrupt内容打断复读 
    if group_id in Interrupt_group:
        random_threshold = Repeat_threshold + randint(0, Repeat_threshold_random_add)
        if Group_Messsage[group_id]['times'] >= random_threshold:
            bot = nonebot.get_bot()
            user_level = 0
            if await SUPERUSER(bot, event): user_level = -1
            elif await GROUP_OWNER(bot, event): user_level = 1
            elif await GROUP_ADMIN(bot, event): user_level = 2
            reply_text = await repeat_interrupt(user_id, user_level)
            await repeat_judger.send(reply_text)
            Group_Messsage[group_id]['times'] -= random_threshold
        
