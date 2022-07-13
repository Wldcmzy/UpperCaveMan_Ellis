from nonebot import require
from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.onebot.v11 import Message
from .config import Config
from .data_source import kaoyan23


global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())


E_scheduler = require("nonebot_plugin_apscheduler").scheduler

@E_scheduler.scheduled_job('cron', hour='1, 8, 18, 20')
async def autosend_noise() -> None:
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    switch_dic = {
        1 : lambda : f'1点乐, 别玩手机乐~',
        8 : kaoyan23,
        18 : lambda : f'8点乐, 我要早八!',
        20 : lambda : f'8点乐, 吃水果~',
    }
    try:
        msg = switch_dic[now.hour]()
        for qqID in plugin_config.noise_qq_friends:
            await bot.send_private_msg(user_id=qqID,message=msg)
        for groupID in plugin_config.noise_qq_groups:
            await bot.send_group_msg(group_id=groupID,message=msg)
    except CQHttpError:
        pass