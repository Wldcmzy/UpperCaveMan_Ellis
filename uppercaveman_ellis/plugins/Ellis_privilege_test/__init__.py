import nonebot
from nonebot import on_command
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from nonebot.params import CommandArg
from nonebot.log import logger
from ..global_args import PRIORITY_NORMAL

E_matcher = on_command(
    "测试权限", 
    aliases={'权限测试'},
    priority=PRIORITY_NORMAL    
)

@E_matcher.handle()
async def _(event: Event, args : Message = CommandArg()):
    if args.extract_plain_text() == '':
        useless, group_id, user_id = event.get_session_id().split('_')
        bot = nonebot.get_bot()
        CQat = f'[CQ:at,qq={user_id}] '
        extra_superuser = " + 原始人" if await SUPERUSER(bot, event) else ''
        if await GROUP_ADMIN(bot, event):
            await E_matcher.send(Message(CQat + "你的权限是: 管理猿" + extra_superuser))
        elif await GROUP_OWNER(bot, event):
            await E_matcher.send(Message(CQat + "你的权限是: 群柱(指巨石阵)" + extra_superuser))
        else:
            await E_matcher.send(Message(CQat + "你的权限是: 万能的群友" + extra_superuser))