from nonebot.adapters.onebot.v11 import Event
from ..global_args import Repeat_judger_args_dic

async def Role_RepeatJudger(event: Event) -> bool:
    session_id = event.get_session_id()
    try :
        useless, group_id, user_id = session_id.split('_')
    except ValueError:
        group_id = '__WTF?'
    return int(group_id) in Repeat_judger_args_dic['privilege']