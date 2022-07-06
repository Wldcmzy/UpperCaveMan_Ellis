from nonebot import require
from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from nonebot.adapters.onebot.v11 import Message
from .config import Config


global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())


E_scheduler = require("nonebot_plugin_apscheduler").scheduler


@E_scheduler.scheduled_job('cron', hour='1, 8, 18, 20')
async def autosend_noise() -> None:
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    switch_dic = {
        1 : '1点乐, 别玩手机乐~',
        8 : '8点乐, 洗脸刷牙出去卷乐~',
        18 : '8点乐, 我要早八!',
        20 : '8点乐, 吃水果~',
    }
    try:
        for qqID in plugin_config.noise_qq_friends:
            await bot.send_private_msg(user_id=qqID,message=Message(switch_dic[now.hour]))
        for groupID in plugin_config.noise_qq_groups:
            await bot.send_group_msg(group_id=groupID,message=Message(switch_dic[now.hour]))
    except CQHttpError:
        pass