from cv2 import log
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import Help_tip
from ..global_args import PRIORITY_NORMAL
from nonebot.log import logger

ClearMine_games = {}
E_help_window = on_command(
    'help', 
    aliases={'帮助'},
    priority=PRIORITY_NORMAL,
)

@E_help_window.handle()
async def clearmine(args : Message = CommandArg()) -> None:
    if args.extract_plain_text() == '':
        reply_text_list = await Help_tip()
        for each_reply_text in reply_text_list:
            await E_help_window.send(each_reply_text)
