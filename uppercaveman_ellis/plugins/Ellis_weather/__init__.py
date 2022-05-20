from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import get_weather
from nonebot.log import logger
from jieba import posseg

E_weather = on_keyword({'天气', 'weather'})

@E_weather.handle()
async def send_weather(event : Event) -> None:
    plain_text = event.get_plaintext().replace('天气', '').replace(' ', '')

    words, city = posseg.lcut(plain_text), None
    for each in words:
        if each.flag == 'ns':
            city = each.word
            break
    
    if city == None: city = plain_text
    reply_text = await get_weather(city)
    await E_weather.finish(reply_text)
