import nonebot
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Event
from nonebot.plugin import PluginMetadata
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11 import Message
from .source_data import get_weather, find_city
from .config import Config


__plugin_meta__ = PluginMetadata(
    name="天气",
    description="查询某地天气",
    usage="天气, weather",
    config=Config
)

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

query_weather = on_keyword({'天气', 'weather'}, priority=15)

@query_weather.handle()
async def _(event : Event) -> None:
    plain_text = event.get_plaintext()
    city = await find_city(plain_text)
    reply_text = await get_weather(city)
    await query_weather.finish(reply_text)


# 消息发送
async def send_weather_info():
    # global msg  # msg改成全局，方便在另一个函数中使用
    msg = await get_weather()
    for qq in plugin_config.weather_qq_friends:
        await nonebot.get_bot().send_private_msg(user_id=qq, message=Message(msg))

    for qq_group in plugin_config.weather_qq_groups:
        await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(msg))  # MessageEvent可以使用CQ发图片


# 定时任务
for index, time in enumerate(plugin_config.weather_inform_time):
    nonebot.logger.info("id:{},time:{}".format(index, time))
    scheduler.add_job(send_weather_info, 'cron', hour=time.hour, minute=time.minute)

