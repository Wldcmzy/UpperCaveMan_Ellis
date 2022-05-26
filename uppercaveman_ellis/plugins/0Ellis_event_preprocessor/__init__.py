# from nonebot.message import event_preprocessor
# from nonebot.adapters.onebot.v11 import MessageEvent
# from nonebot.exception import IgnoredException
# from ..global_args import PerUser_Response_CD
# import time

# User_Last_Say_Time = {}

# @event_preprocessor
# async def do_something(event : MessageEvent):
#     event_session = event.get_session_id()
#     user_id = '-1'
#     if '_' in event_session:
#         useless, group_id, user_id = event_session.split('_')
#     else:
#         user_id = event_session
    
#     now_time = time.time()
#     if user_id not in User_Last_Say_Time:
#         User_Last_Say_Time[user_id] = now_time
#     else:
#         if now_time - User_Last_Say_Time[user_id] < PerUser_Response_CD:
#             raise IgnoredException('机器人响应每个用户有冷却时间限制')
#         else:
#             User_Last_Say_Time[user_id] = now_time

