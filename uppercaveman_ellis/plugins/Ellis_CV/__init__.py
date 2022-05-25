from os import stat
from cv2 import log
from nonebot import on_command
from nonebot.params import CommandArg, Arg, ArgStr
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.log import logger
from .privilege import Role_CV
from .source_data import ( 
    E_binary,
    E_blur,
    E_canny,
    E_fliphalf,
    get_1st_pic_url,
    download_pic, 
    E_flip, 
    E_gray,
)

#===============================================
# 图片反转/反转一半

E_cv_flip = on_command('flip', rule=Role_CV)
@E_cv_flip.handle()
async def cv_flip_pre(event : Event, state: T_State) -> None:
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    state['operation'] = msg.strip()[ : 10].lower()
    if url: 
        state['url'] = url
        state['new_msg'] = True

@E_cv_flip.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cv_flip(state : T_State, url = Arg('url'), op : str = Arg('operation')):

    if url is None: 
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    CQname = '没有图'
    if url:
        fname = await download_pic(url)
        if op[ : 8] == 'fliphalf':
            method = 'u'
            if len(op) > 8 and op[8] in 'lrud': method = op[8]
            CQname = await E_fliphalf(fname, method)
        else:
            axis = -1
            if op[ : 6] != 'flipxy':
                if op[ : 5] == 'flipx': axis = 1
                elif op[ : 5] == 'flipy' : axis = 0
            CQname = await E_flip(fname, axis)
            
    await E_cv_flip.finish(Message(CQname))


# ================================================
# 生成灰度图
E_cv_gray = on_command('gray', rule=Role_CV)
@E_cv_gray.handle()
async def cv_gray_pre(event : Event, state : T_State) -> None:
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        state['url'] = url
        state['new_msg'] = True

@E_cv_gray.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cv_gray(state : T_State, url = Arg('url')):
    if url is None:
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    if url:
        fname = await download_pic(url)
        CQname = await E_gray(fname)
        await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')


E_cv_binary = on_command('binary', rule=Role_CV)
@E_cv_binary.handle()
async def cv_binary_pre(event : Event, state : T_State) -> None:
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    state['method'] = msg.strip()[ : 7].lower()
    if url:
        state['url'] = url
        state['new_msg'] = True

@E_cv_binary.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cv_binary(state : T_State, url = Arg('url'), method_text : str = Arg('method')):
    if url is None:
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    CQname = '没有图'
    if url:
        method = 1
        try: 
            method = int(method_text[6]) 
        except: 
            pass
        fname = await download_pic(url)
        CQname = await E_binary(fname, method)
    await E_cv_flip.finish(Message(CQname))

E_cv_blur = on_command('blur', rule=Role_CV)
@E_cv_blur.handle()
async def cv_blur_pre(event : Event, state : T_State) -> None:
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    state['method'] = msg.strip()[ : 5].lower()
    if url:
        state['url'] = url
        state['new_msg'] = True

@E_cv_blur.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cv_blur(state : T_State, url = Arg('url'), method_text : str = Arg('method')):
    if url is None:
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    CQname = '没有图'
    if url:
        method = 1
        try : 
            method = int(method_text[4])
        except:
            pass
        fname = await download_pic(url)
        CQname = await E_blur(fname, method)
    await E_cv_flip.finish(Message(CQname))


E_cv_canny = on_command('canny', rule=Role_CV)
@E_cv_canny.handle()
async def cv_canny_pre(event : Event, state : T_State) -> None:
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        state['url'] = url
        state['new_msg'] = True

@E_cv_canny.got('new_msg', prompt='没找到图片, 请给我张图...')
async def cv_canny(state : T_State, url = Arg('url')):
    if url is None:
        new_msg = str(state['new_msg'])
        url = await get_1st_pic_url(new_msg)

    CQname = '没有图'
    if url:
        fname = await download_pic(url)
        CQname = await E_canny(fname)
        
    await E_cv_flip.finish(Message(CQname))