from nonebot import require
from datetime import datetime
import nonebot
import pytz
from aiocqhttp.exceptions import Error as CQHttpError
from ..global_args import Weather_autosend_groups_dic, Noise_autosend_groups
from ..Ellis_weather import get_weather

E_scheduler = require("nonebot_plugin_apscheduler").scheduler

@E_scheduler.scheduled_job('cron', hour='6, 12, 17')
async def autosend_weather() -> None:
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    try:
        for groupID, city in Weather_autosend_groups_dic.items():
            msg = f'{now.hour}点乐~\n' + await get_weather(city)
            await bot.send_group_msg(group_id=groupID,message=msg)
    except CQHttpError:
        pass

@E_scheduler.scheduled_job('cron', hour='1, 8, 18, 20')
async def autosend_noise() -> None:
    bot = nonebot.get_bot()
    now = datetime.now(pytz.timezone('Asia/Shanghai'))
    switch_dic = {
        1 : '1点乐, 别玩收集乐~',
        8 : '8点乐, 洗脸刷牙出去卷乐~',
        18 : '8点乐, 我要早八!',
        20 : '8点乐, 吃水果~',
    }
    try:
        for groupID in Noise_autosend_groups:
            await bot.send_group_msg(group_id=groupID,message=switch_dic[now.hour])
    except CQHttpError:
        pass