from nonebot.adapters.onebot.v11 import Event
from ..global_args import CV_groups

async def Role_CV(event: Event) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = -1
    return int(group_id) in CV_groups