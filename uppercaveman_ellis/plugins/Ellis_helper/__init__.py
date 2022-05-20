from cv2 import log
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import Help_tip
from nonebot.log import logger

ClearMine_games = {}
E_help_window = on_command('help', aliases={'帮助'})

@E_help_window.handle()
async def clearmine(args : Message = CommandArg()) -> None:
    if args.extract_plain_text() == '':
        reply_text = await Help_tip()
        await E_help_window.finish(reply_text)
