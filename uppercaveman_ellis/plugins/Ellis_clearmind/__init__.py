from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import ClearMine
from .privilege import Role_clearmine
from ..global_args import PRIORITY_NORMAL
from nonebot.log import logger

ClearMine_games = {}
E_clearmind = on_command('clearmine',
                aliases={'clearmind', '扫雷', '明镜止水之心'}, 
                rule=Role_clearmine,
                priority=PRIORITY_NORMAL,
            )

@E_clearmind.handle()
async def clearmine(event: Event, args : Message = CommandArg()) -> None:
    group_id = int(event.get_session_id().split('_')[1])
    if group_id not in ClearMine_games: 
        ClearMine_games[group_id] = ClearMine()
    operation = args.extract_plain_text()
    reply_text = ClearMine_games[group_id].parseOP(operation)
    await E_clearmind.finish(Message(reply_text))
