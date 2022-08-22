from nonebot.rule import to_me
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message, GROUP
from nonebot.params import CommandArg
from .data_source import memo_add,memo_del,memo_see
import nonebot
from .config import Config
from nonebot_plugin_apscheduler import scheduler
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from nonebot.permission import SUPERUSER
from nonebot.log import logger


async def __user_privilege(event: Event) -> int:
    bot = nonebot.get_bot()
    if await SUPERUSER(bot, event):
        logger.debug('\n\n\n SUPERUSER \n\n\n')
        return 0
    elif await GROUP_ADMIN(bot, event) or await GROUP_OWNER(bot, event):
        logger.debug('\n\n\n 111111111 \n\n\n')
        return 1
    else:
        return 2

global_config = nonebot.get_driver().config
plugin_config = Config(**global_config.dict())

memorandum_add = on_command('写入', aliases={'记录'},permission=GROUP,rule=to_me(),priority=8,)
memorandum_del = on_command('删除', permission=GROUP,rule=to_me(),priority=8,)
memorandum_see = on_command('查看', permission=GROUP,aliases={'备忘录'},priority=8,)

@memorandum_add.handle()
async def _(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_text = args.extract_plain_text()
    reply_text = memo_add(group_id, user_id, plain_text, await __user_privilege(event))
    await memorandum_add.finish(reply_text)

@memorandum_del.handle()
async def memorandum_delete(event : Event, args : Message = CommandArg()) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    plain_index = args.extract_plain_text()
    reply_text = memo_del(group_id, plain_index, user_id, await __user_privilege(event))
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


async def memo_auto_send():
    for qq_group in plugin_config.memo_qq_groups:
        msg = memo_see(str(qq_group))
        if not msg: return 
        if type(msg) == list:
            if not msg: return
            await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message("备忘录内容记得完成~"))
            for piece in msg:
                await nonebot.get_bot().send_group_msg(group_id=qq_group, message=Message(piece))
# 定时任务
for index, time in enumerate(plugin_config.memo_inform_time):
    scheduler.add_job(memo_auto_send, 'cron', hour=time.hour, minute=time.minute)
