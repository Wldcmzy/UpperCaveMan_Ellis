from nonebot.adapters.onebot.v11 import Event
from ..global_args import ClearMine_groups
from nonebot.log import logger

async def Role_clearmine(event: Event) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = '__WTF?'
    return int(group_id) in ClearMine_groups
