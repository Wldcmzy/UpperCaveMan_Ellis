from nonebot.rule import to_me
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message, GROUP
from nonebot.params import CommandArg
from .data_source import memo_add,memo_del,memo_see
memorandum_add = on_command(
    '写入', 
    aliases={'记录'},
    permission=GROUP,
    rule=to_me(),
    priority=8,
)
memorandum_del = on_command(
    '删除', 
    permission=GROUP,
    rule=to_me(),
    priority=8,
)
memorandum_see = on_command(
    '查看', 
    permission=GROUP,
    aliases={'备忘录'},
    priority=8,
)

@memorandum_add.handle()
async def _(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_text = args.extract_plain_text()
    reply_text = memo_add(group_id, user_id, plain_text)
    await memorandum_add.finish(reply_text)

@memorandum_del.handle()
async def memorandum_delete(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_index = args.extract_plain_text()
    reply_text = memo_del(group_id, plain_index)
    await memorandum_del.finish(reply_text)

@memorandum_see.handle()
async def memorandum_read(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    reply = memo_see(group_id)
    if type(reply) == list:
        if reply == []:
            await memorandum_see.finish('暂无备忘录信息')
        for piece in reply:
            await memorandum_see.send(piece)
    else:
        await memorandum_see.finish(reply)