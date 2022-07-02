from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .data_source import rand_speaker

rand_maker = on_command('rand', aliases={'随机'}, priority=15)

@rand_maker.handle()
async def _(args : Message = CommandArg()) -> None:    
    plain_text = args.extract_plain_text()
    reply_text = await rand_speaker(plain_text)
    await rand_maker.finish(reply_text)