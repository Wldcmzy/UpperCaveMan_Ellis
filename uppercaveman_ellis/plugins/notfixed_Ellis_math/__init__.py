from nonebot.exception import FinishedException
from nonebot.log import logger
from .source_data import int_sure, gcd, isprime, lcm, power, inverse_exgcd, inverse_Fermat
from nonebot import on_command
from nonebot.params import CommandArg, RawCommand
from nonebot.adapters.onebot.v11 import Event, Message

math_gcd = on_command('gcd', priority=10)
@E_math.handle()
async def do_math(cmd : str = RawCommand(), arg_input : Message = CommandArg()) -> None:
    try:
        ret = ''
        arg_input = arg_input.extract_plain_text()
        syntex = cmd + ' ' + arg_input
        args = arg_input.split()
        if cmd == 'inv':
            if args[0] == 'fm':
                syntex = '此功能不会做任何特判, 谨慎使用~\n' + syntex
                ret = await inverse_Fermat(int_sure(args[1]), int_sure(args[2]))
            else:
                ret = await inverse_exgcd(int_sure(args[0]), int_sure(args[1]))
        elif cmd == 'gcd':
            ret = await gcd(int_sure(args[0]), int_sure(args[1]))
        elif cmd == 'lcm':
            ret = await lcm(int_sure(args[0]), int_sure(args[1]))
        elif cmd == 'pow':
            syntex += r'(%998244353)'
            ret = await power(int_sure(args[0]), int_sure(args[1]))
        elif cmd == 'isprime':
            syntex += r'(%998244353)'
            ret = await isprime(int_sure(args[0]))
        else:
            raise Exception(f'无效命令:{cmd}')
        await E_math.finish(syntex + ' 是:' + str(ret))
    except FinishedException:
        pass
    except Exception as e:
        await E_math.finish('呜呜呜~ 出错了:\n' + str(type(e)) + ': ' + str(e))

