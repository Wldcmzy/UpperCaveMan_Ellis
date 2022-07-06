from argparse import Namespace
from tokenize import group
from nonebot.rule import ArgumentParser
from nonebot import on_command, on_shell_command
from nonebot.adapters.onebot.v11 import Event, Message, GROUP
from nonebot.params import CommandArg, ShellCommandArgs
from nonebot.exception import FinishedException
from .data_source import ClearMine
from nonebot.log import logger

ClearMine_games: dict[str, ClearMine] = {}

parser_clearmind = ArgumentParser("扫雷", description="扫雷")
parser_clearmind.add_argument("--stop", action="store_true", help="停止扫雷")
parser_clearmind.add_argument("-c", "--cfg", action="store_true", help = "场地大小")
parser_clearmind.add_argument("-s", "--show", action="store_true", help = "查看场地")
parser_clearmind.add_argument("input", nargs="*", help="扫雷输入")
clearmind = on_shell_command('扫雷',
                permission=GROUP,
                parser=parser_clearmind,
                priority=11,
            )

@clearmind.handle()
async def _(event: Event, args : Namespace = ShellCommandArgs()) -> None:
    args = vars(args)
    if args['cfg'] + args['show'] + args['stop'] >= 2: 
        await clearmind.finish('指令冲突...')

    useless, group_id, user_id = event.get_session_id().split('_')

    if args['stop']:
        if group_id in ClearMine_games:
            del ClearMine_games[group_id]
            await clearmind.finish('扫雷游戏结束~')
        else:
            clearmind.finish('并没有在进行的扫雷游戏~')

    mode = 'click'
    if args['cfg']: mode = 'cfg'
    if args['show']: mode = 'show'

    if group_id not in ClearMine_games: 
        ClearMine_games[group_id] = ClearMine(group_id)
        await clearmind.send('没有正在进行的扫雷游戏, 创建一个新的~\n首次点击之后生成地雷~')

    if len(args['input']) != 2:
        if mode in ['cfg']: 
            await clearmind.finish('config参数数量有误, 应该为2个参数')
        elif mode in ['click']:
            raise FinishedException

    reply = ClearMine_games[group_id].parseOP(args['input'], mode)
    await clearmind.finish(reply)

    

    
