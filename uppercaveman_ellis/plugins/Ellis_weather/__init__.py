from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import get_weather
from nonebot.log import logger

E_weather = on_command('天气')

@E_weather.handle()
async def send_weather(event : Event, args : Message = CommandArg()) -> None:
    # plain_text = event.get_plaintext()
    plain_text = args.extract_plain_text()
    reply_text = await get_weather(plain_text)
    await E_weather.finish(reply_text)
