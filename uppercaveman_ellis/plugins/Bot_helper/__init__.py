from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from nonebot.log import logger
from .data_source import Help_tip

need_help = on_command(
    'help', 
    aliases={'帮助'},
    priority=10,
)

@need_help.handle()
async def _(args : Message = CommandArg()) -> None:
    if args.extract_plain_text() == '':
        reply_text_list = await Help_tip()
        for each_reply_text in reply_text_list:
            await need_help.send(each_reply_text)
