from nonebot.rule import ArgumentParser
from nonebot.exception import FinishedException
from .data_source import gcd, isprime, lcm, power, inverse_exgcd, inverse_Fermat, Default_Mod
from nonebot import on_command, on_shell_command
from nonebot.params import CommandArg, RawCommand, ShellCommandArgv, ShellCommandArgs
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.log import logger
import math
from typing import Optional, Union, List

MATH_Priority = 8
extra_head_int = f'输入数据均对{Default_Mod}取模, 答案是:'

query_PI = on_command('圆周率', priority=MATH_Priority)
query_E = on_command('欧拉数', priority=MATH_Priority)
query_gcd = on_command('gcd', priority=MATH_Priority)
query_lcm = on_command('lcm', priority=MATH_Priority)
query_pow = on_command('pow', priority=MATH_Priority)
query_isprime = on_command('isprime', priority=MATH_Priority)

parser_inv = ArgumentParser("inv", description="逆元")
parser_inv.add_argument("-m", "--mode", type=str, default='exgcd', help="求解方式")
parser_inv.add_argument("values", nargs="+", help="需要计算的数")
query_inv = on_shell_command('inv', parser=parser_inv, priority=MATH_Priority)

@query_PI.handle()
async def _(args : Message = CommandArg()) -> None:
    if not args.extract_plain_text().strip():
        await query_PI.finish(f'π约等于{math.pi}')

@query_E.handle()
async def _(args : Message = CommandArg()) -> None:
    if not args.extract_plain_text().strip():
        await query_PI.finish(f'e约等于{math.e}')

@query_gcd.handle()
async def _(args : Message = CommandArg()) -> None:
    args = args.extract_plain_text().strip().split()
    if len(args) != 2: await query_gcd.finish('参数数量有误, 请输入2个参数')
    await query_gcd.finish(extra_head_int + str(await gcd(*args)))
    
@query_lcm.handle()
async def _(args : Message = CommandArg()) -> None:
    args = args.extract_plain_text().strip().split()
    if len(args) != 2: await query_gcd.finish('参数数量有误, 请输入2个参数')
    await query_gcd.finish(extra_head_int + str(await lcm(*args)))

@query_pow.handle()
async def _(args : Message = CommandArg()) -> None:
    args = args.extract_plain_text().strip().split()
    if len(args) not in (2, 3): await query_gcd.finish('参数数量有误, 请输入2或3个参数')
    await query_gcd.finish(extra_head_int + str(await power(*args)))

@query_isprime.handle()
async def _(args : Message = CommandArg()) -> None:
    args = args.extract_plain_text().strip().split()
    if len(args) != 1: await query_gcd.finish('参数数量有误, 请输入1个参数')
    await query_gcd.finish(extra_head_int + str(await isprime(*args)))

@query_inv.handle()
async def _(args = ShellCommandArgs()) -> None:
    try:
        args = vars(args)
        logger.debug(f'>>>>>>>>>>>>{args}')
    except Exception as e:
        await query_inv.finish(f'输入格式有误{type(e)}:{str(e)}')
    
    if len(args['values']) != 2: await query_gcd.finish('参数数量有误, 请输入2个参数')
    if args['mode'] == 'exgcd':
        await query_gcd.finish(extra_head_int + str(await inverse_exgcd(*args['values'])))
    elif args['mode'] == 'fm':
        await query_gcd.finish(extra_head_int + str(await inverse_Fermat(*args['values'])) + '\n此方法不验证数据合法性, 请谨慎使用')
    else:
        await query_gcd.finish('mode 参数有误')

