from nonebot import on_command
from nonebot.params import CommandArg
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


E_cv_flip = on_command('flip', rule=Role_CV)
@E_cv_flip.handle()
async def cv_flip(event : Event) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        msg = msg.strip().lower()
        fname = await download_pic(url)        
        if msg[ : 8] == 'fliphalf':
            method = 'u'
            if msg[8] in 'lrud':
                method = msg[8]
            CQname = await E_fliphalf(fname, method)
            await E_cv_flip.finish(Message(CQname))
        else:
            axis = -1
            if msg[ : 6] != 'flipxy':
                if msg[ : 5] == 'flipx': axis = 0
                elif msg[ : 5] == 'flipy' : axis = 1
            CQname = await E_flip(fname, axis)
            await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')


E_cv_gray = on_command('gray', rule=Role_CV)
@E_cv_gray.handle()
async def cv_gray(event : Event) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        fname = await download_pic(url)
        CQname = await E_gray(fname)
        await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')


E_cv_gray = on_command('binary', rule=Role_CV)
@E_cv_gray.handle()
async def cv_gray(event : Event) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        msg = msg.strip().lower()
        method = 1
        try : 
            method = int(msg[6])
        except:
            pass
        fname = await download_pic(url)
        CQname = await E_binary(fname, method)
        await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')

E_cv_gray = on_command('blur', rule=Role_CV)
@E_cv_gray.handle()
async def cv_gray(event : Event) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        msg = msg.strip().lower()
        method = 1
        try : 
            method = int(msg[4])
        except:
            pass
        fname = await download_pic(url)
        CQname = await E_blur(fname, method)
        await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')


E_cv_gray = on_command('canny', rule=Role_CV)
@E_cv_gray.handle()
async def cv_gray(event : Event) -> None:
    useless, group_id, user_id = event.get_session_id().split('_')
    group_id, user_id = int(group_id), int(user_id)
    msg = str(event.get_message())
    url = await get_1st_pic_url(msg)
    if url:
        fname = await download_pic(url)
        CQname = await E_canny(fname)
        await E_cv_flip.finish(Message(CQname))
    else :
        await E_cv_flip.finish('没有图')