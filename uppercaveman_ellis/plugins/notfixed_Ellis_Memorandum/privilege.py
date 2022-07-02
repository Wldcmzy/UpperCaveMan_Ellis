import nonebot
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from ..global_args import Memorandum_groups_users
from nonebot.log import logger

async def Role_memorandum_modify(event: GroupMessageEvent) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = -1
    
    group_id = int(group_id)
    if group_id in Memorandum_groups_users:
        logger.debug(str(event.get_session_id()))
        bot = nonebot.get_bot()
        if await SUPERUSER(bot, event):
            return True
        if Memorandum_groups_users[group_id]['allow_owner']:
            if await GROUP_OWNER(bot, event):
                return True
        if Memorandum_groups_users[group_id]['allow_admin']:
            if await GROUP_ADMIN(bot, event):
                return True
        return int(user_id) in Memorandum_groups_users[group_id]['allow_users']
    return False

async def Role_memorandum_read(event: GroupMessageEvent) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = -1
    
    return int(group_id) in Memorandum_groups_users
