
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .privilege import Role_Memorandum
from nonebot.log import logger

E_memorandum_write = on_command(
    '写入', 
    aliases={'记录'}, 
    rule=Role_Memorandum,
)

@E_memorandum_write.handle()
async def memorandum_write(args : Message = CommandArg()) -> None:
    pass


E_memorandum_delete = on_command(
    '删除', 
    rule=Role_Memorandum,
)

@E_memorandum_delete.handle()
async def memorandum_delete(args : Message = CommandArg()) -> None:
    pass


E_memorandum_read = on_command(
    '查看备忘录', 
    aliases={'查备忘录', '看备忘录'},
)

@E_memorandum_read.handle()
async def memorandum_read(args : Message = CommandArg()) -> None:
    pass