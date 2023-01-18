from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg, Arg
from nonebot.typing import T_State
from .data_source import query, query_directly
from nonebot.log import logger
from nonebot.exception import FinishedException

baike = on_command('百科', aliases={'查询','baike'},priority=10)

@baike.handle()
async def q(state: T_State, event : Event, args : Message = CommandArg()):
    plain_text = args.extract_plain_text()

    code, reply, extra = query(plain_text)

    if code != 0:
        await baike.finish(f'错误码:{code},{reply}')

    if extra == None:
        await baike.finish(reply)
    else:
        state['extra'] = extra
        reply_mean, reply_optional = reply.split('|')
        await baike.send(reply_mean.strip())
        await baike.send(reply_optional.strip())
    
@baike.got('index')
async def qd(state : T_State, extra = Arg('extra')):

    try:
        index = int(str(state['index']))
        assert index >= 0 and index <= len(extra)
    except Exception as e:
        await baike.finish(f'序号错误, 查询终止\n{type(e)} | {str(e)}')
    
    if index == 0:
        await baike.finish('本轮查询结束')
    
    code, reply = query_directly(extra[index - 1])

    if code != 0:
        await baike.finish(f'错误码:{code},{reply}')

    await baike.finish(reply)
