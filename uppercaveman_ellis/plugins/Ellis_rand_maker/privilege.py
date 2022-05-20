from nonebot.adapters.onebot.v11 import Event
from ..global_args import Rand_groups

async def Role_rand(event: Event) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = '__WTF?'
    return int(group_id) in Rand_groups
