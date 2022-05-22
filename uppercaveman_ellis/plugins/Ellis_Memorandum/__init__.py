# 基于txt文件的轻量备忘录, 无数据库
from nonebot.rule import to_me, Rule
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .privilege import Role_memorandum_modify, Role_memorandum_read
from nonebot.log import logger
import os
from ..global_args import Memorandum_data_path
from .source_data import file_delete, file_read, file_write
E_memorandum_write = on_command(
    '写入', 
    aliases={'记录'}, 
    rule=to_me() & Rule(Role_memorandum_modify),
)

@E_memorandum_write.handle()
async def memorandum_write(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_text = args.extract_plain_text()
    reply_text = file_write(group_id, plain_text)
    await E_memorandum_write.finish(reply_text)

    

E_memorandum_delete = on_command(
    '删除', 
    rule=to_me() & Rule(Role_memorandum_modify),
)

@E_memorandum_delete.handle()
async def memorandum_delete(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_text = args.extract_plain_text()
    reply_text = file_delete(group_id, plain_text)
    await E_memorandum_delete.finish(reply_text)



E_memorandum_read = on_command(
    '查看备忘录', 
    rule =to_me() & Rule(Role_memorandum_read),
    aliases={'查备忘录', '看备忘录', '查看'},
)

@E_memorandum_read.handle()
async def memorandum_read(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    reply_text = file_read(group_id)
    await E_memorandum_read.finish(reply_text)