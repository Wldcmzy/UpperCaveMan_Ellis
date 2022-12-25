
from nonebot import on_command, on_shell_command
from nonebot.params import CommandArg, Arg, ArgStr, ShellCommandArgs
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Message, GROUP
from nonebot.log import logger
from nonebot.rule import ArgumentParser
from argparse import Namespace
from .data_source import get_1st_pic_url, execute, modes

parser_cv = ArgumentParser("cv", description="cv")
parser_cv.add_argument("input", nargs="*", help="cv参数")

Ez_CV = on_shell_command(
    'cv',
    aliases={'CV', '图像处理'},
    permission=GROUP,
    parser=parser_cv,
    priority=20,
)

@Ez_CV.handle()
async def cvprepare(event: Event, state: T_State, args : Namespace = ShellCommandArgs()) -> None:
    args = vars(args)
    args: list[str] = args['input']

    for i in range(len(args)):
        if '[CQ' in args[i]:
            del args[i]
            break

    if len(args) < 1:
        await Ez_CV.finish(f'请在命令中加入模式, 模式有:\n{str(list(modes.keys()))}')
    mode = args[0]
    if mode not in modes.keys(): 
        await Ez_CV.finish(f'模式错误, 模式有:\n{str(list(modes.keys()))}')

    state['mode'] = mode
    state['extra'] = args[1 : ]

    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)    
    if url: 
        state['url'] = url
        state['new_msg'] = True
    

@Ez_CV.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cvwork(state : T_State, url = Arg('url'), mode : str = Arg('mode'), extra: list = Arg('extra')):
    if url is None:
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    ret = '没有图'
    if url:
        arg = None
        
        if len(extra) >= 1:
            if extra[0] not in modes[mode]:
                await Ez_CV.finish(f'参数错误, 参数值有:\n{modes[mode]}')
            else:
                arg = extra[0]
        

        if len(extra) == 0:
            if len(modes[mode]) > 0:
                await Ez_CV.send(f'未设置参数, 默认使用"{modes[mode][0]}", 参数值有:{modes[mode]}')
                arg = modes[mode][0]

        ret = await execute(url, mode, arg)

    await Ez_CV.finish(Message(ret))

        

# # ==============================================
# # 图片反转/反转一半

# E_cv_flip = on_command(
#     'flip', 
#     priority=CV_priority,
# )
# @E_cv_flip.handle()
# async def cv_flip_pre(event : Event, state: T_State) -> None:
#     msg = str(event.get_message())
#     url = await get_1st_pic_url(msg)
#     state['operation'] = msg.strip()[ : 10].lower()
#     if url: 
#         state['url'] = url
#         state['new_msg'] = True

# @E_cv_flip.got('new_msg', prompt='没找到图片, 请给我张图...')
# async def cv_flip(state : T_State, url = Arg('url'), op : str = Arg('operation')):

#     if url is None: 
#         new_msg = str(state['new_msg'])
#         url = await get_1st_pic_url(new_msg)

#     CQname = '没有图'
#     if url:
#         fname = await download_pic(url)
#         if op[ : 8] == 'fliphalf':
#             method = 'u'
#             if len(op) > 8 and op[8] in 'lrud': method = op[8]
#             CQname = await E_fliphalf(fname, method)
#         else:
#             axis = -1
#             if op[ : 6] != 'flipxy':
#                 if op[ : 5] == 'flipx': axis = 1
#                 elif op[ : 5] == 'flipy' : axis = 0
#             CQname = await E_flip(fname, axis)
            
#     await E_cv_flip.finish(Message(CQname))


# # ================================================
# # 生成灰度图
# E_cv_gray = on_command(
#     'gray', 
#     priority=CV_priority,
# )
# @E_cv_gray.handle()
# async def cv_gray_pre(event : Event, state : T_State) -> None:
#     msg = str(event.get_message())
#     url = await get_1st_pic_url(msg)
#     if url:
#         state['url'] = url
#         state['new_msg'] = True

# @E_cv_gray.got('new_msg', prompt='没找到图片, 请给我张图...')
# async def cv_gray(state : T_State, url = Arg('url')):
#     if url is None:
#         new_msg = str(state['new_msg'])
#         url = await get_1st_pic_url(new_msg)

#     if url:
#         fname = await download_pic(url)
#         CQname = await E_gray(fname)
#         await E_cv_flip.finish(Message(CQname))
#     else :
#         await E_cv_flip.finish('没有图')


# # ==============================================
# # 图片二值化
# E_cv_binary = on_command(
#     'binary', 
#     priority=CV_priority,
# )
# @E_cv_binary.handle()
# async def cv_binary_pre(event : Event, state : T_State) -> None:
#     msg = str(event.get_message())
#     url = await get_1st_pic_url(msg)
#     state['method'] = msg.strip()[ : 7].lower()
#     if url:
#         state['url'] = url
#         state['new_msg'] = True

# @E_cv_binary.got('new_msg', prompt='没找到图片, 请给我张图...')
# async def cv_binary(state : T_State, url = Arg('url'), method_text : str = Arg('method')):
#     if url is None:
#         new_msg = str(state['new_msg'])
#         url = await get_1st_pic_url(new_msg)

#     CQname = '没有图'
#     if url:
#         method = 1
#         try: 
#             method = int(method_text[6]) 
#         except: 
#             pass
#         fname = await download_pic(url)
#         CQname = await E_binary(fname, method)
#     await E_cv_flip.finish(Message(CQname))


# # ==============================================
# # 图片滤波
# E_cv_blur = on_command(
#     'blur', 
#     priority=CV_priority,
# )
# @E_cv_blur.handle()
# async def cv_blur_pre(event : Event, state : T_State) -> None:
#     msg = str(event.get_message())
#     url = await get_1st_pic_url(msg)
#     state['method'] = msg.strip()[ : 5].lower()
#     if url:
#         state['url'] = url
#         state['new_msg'] = True

# @E_cv_blur.got('new_msg', prompt='没找到图片, 请给我张图...')
# async def cv_blur(state : T_State, url = Arg('url'), method_text : str = Arg('method')):
#     if url is None:
#         new_msg = str(state['new_msg'])
#         url = await get_1st_pic_url(new_msg)

#     CQname = '没有图'
#     if url:
#         method = 1
#         try : 
#             method = int(method_text[4])
#         except:
#             pass
#         fname = await download_pic(url)
#         CQname = await E_blur(fname, method)
#     await E_cv_flip.finish(Message(CQname))

# # ==============================================
# # canny边缘检测
# E_cv_canny = on_command(
#     'canny', 
#     priority=CV_priority,
# )
# @E_cv_canny.handle()
# async def cv_canny_pre(event : Event, state : T_State) -> None:
#     msg = str(event.get_message())
#     url = await get_1st_pic_url(msg)
#     if url:
#         state['url'] = url
#         state['new_msg'] = True

# @E_cv_canny.got('new_msg', prompt='没找到图片, 请给我张图...')
# async def cv_canny(state : T_State, url = Arg('url')):
#     if url is None:
#         new_msg = str(state['new_msg'])
#         url = await get_1st_pic_url(new_msg)

#     CQname = '没有图'
#     if url:
#         fname = await download_pic(url)
#         CQname = await E_canny(fname)
        
#     await E_cv_flip.finish(Message(CQname))