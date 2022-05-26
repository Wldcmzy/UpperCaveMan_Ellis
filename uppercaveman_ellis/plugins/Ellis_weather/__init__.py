from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import get_weather, find_city
from nonebot.log import logger
from ..global_args import PRIORITY_NORMAL


E_weather = on_keyword(
    {'天气', 'weather'},
    priority=PRIORITY_NORMAL
)

@E_weather.handle()
async def send_weather(event : Event) -> None:
    plain_text = event.get_plaintext()
    city = await find_city(plain_text)
    reply_text = await get_weather(city)
    await E_weather.finish(reply_text)
