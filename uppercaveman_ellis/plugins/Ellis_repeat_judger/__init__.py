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

# 提取阈值信息
Repeat_threshold = plugin_config.repeat_judger_threshold
Repeat_threshold_random_add = plugin_config.repeat_judge_threshold_random_add

# 提取分组信息
Whisper_group = set(plugin_config.repeat_judger_group)
Interrupt_group = set(plugin_config.repeat_judger_group_interrupt)

# 建议先令各分组集合互斥，使得增加分组后的完成逻辑变得容易
# 此处为打断模式优先保留
Whisper_group -= Interrupt_group


Group_Messsage = {}

repeat_judger = on_message(permission=GROUP, priority=90)

@repeat_judger.handle()
async def _(event : Event) -> None:

    useless, group_id, user_id = event.get_session_id().split('_')
    msg = await remove_image_num(str(event.get_message()))

    # 若消息集合中没有这个群的信息, 新建一个
    if group_id not in Group_Messsage: 
        Group_Messsage[group_id] = {'text' : msg, 'times' : 0}

    
    # 若信息变换的情况
    if Group_Messsage[group_id]['text'] != msg:


        #对于Whisper分组,判断是否达成复读条件，然后执行响应操作
        if group_id in Whisper_group and Group_Messsage[group_id]['times'] >= Repeat_threshold:
            relpy_text = await repeat_whisper(user_id, Group_Messsage[group_id]['times'])
            await repeat_judger.send(relpy_text)
        # 因信息改变，应重置消息计数
        Group_Messsage[group_id] = {'text' : msg, 'times' : 0}


        # if group_id in costum_group:
        #   ...
        #
        # if group_id in diy_group:
        #   ...



    # 若信息不变的情况
    else:
        Group_Messsage[group_id]['times'] += 1

        # 对于Interrupt分组, 若达成条件, 发送interrupt内容打断复读 
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

        # if group_id in costum_group:
        #   ...
        #
        # if group_id in diy_group:
        #   ...
        
