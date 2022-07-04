import requests
from .config import Config
from nonebot import require
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
import nonebot
from nonebot.adapters.onebot.v11 import Message, MessageSegment
from pathlib import Path

S60_PATH: Path = Path(__file__).parent / "resource"

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())
scheduler = require("nonebot_plugin_apscheduler").scheduler  # type:AsyncIOScheduler

def remove_upprintable_chars(s):
    return ''.join(x for x in s if x.isprintable())#去除imageUrl可能存在的不可见字符

async def read60s():
    #global msg  # msg改成全局，方便在另一个函数中使用
    msg = await suijitu()
    for qq in plugin_config.daily_qq_friends:
        await nonebot.get_bot().send_private_msg(user_id=qq, message=Message(msg))

    for qq_group in plugin_config.daily_qq_groups:
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(msg))# MessageEvent可以使用CQ发图片



async def suijitu():
    try:
        url="https://api.iyk0.com/60s"
        resp = requests.get(url)
        resp = resp.text
        resp = remove_upprintable_chars(resp)
        retdata = json.loads(resp)
        lst = retdata['imageUrl']
        with open(S60_PATH / "read60s.png", 'wb') as f:
            f.write(requests.get(lst).content)
        img = MessageSegment.image(f'file://{S60_PATH / "read60s.png"}')
        pic_ti = f"今日60S读世界已送达\n[CQ:image,file={img}]"
        return pic_ti
    except:
        url = "https://api.2xb.cn/zaob"#备用网址
        resp = requests.get(url)
        resp = resp.text
        resp = remove_upprintable_chars(resp)
        retdata = json.loads(resp)
        lst = retdata['imageUrl']
        with open(S60_PATH / "read60s.png", 'wb') as f:
            f.write(requests.get(lst).content)
        img = MessageSegment.image(f'file://{S60_PATH / "read60s.png"}')
        pic_ti1 = f"今日60S读世界已送达\n[CQ:image,file={img}]"
        return pic_ti1

for index, time in enumerate(plugin_config.daily_inform_time):
    scheduler.add_job(read60s, "cron", hour=time.hour, minute=time.minute)
