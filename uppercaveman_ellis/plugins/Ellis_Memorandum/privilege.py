import nonebot
from nonebot.permission import SUPERUSER
from nonebot.adapters.onebot.v11 import Event
from nonebot.adapters.onebot.v11 import GROUP_ADMIN, GROUP_OWNER
from ..global_args import Memorandum_groups_users
from nonebot.log import logger

async def Role_Memorandum(event: Event) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = -1
    
    if int(group_id) in Memorandum_groups_users:
        bot = nonebot.get_bot()
        if SUPERUSER(bot, event):
            return True
        if Memorandum_groups_users['allow_owner']:
            if GROUP_OWNER(bot, event):
                return True
        if Memorandum_groups_users['allow_admin']:
            if GROUP_ADMIN(bot, event):
                return True
        return int(user_id) in Memorandum_groups_users['allow_users']
    return False