from random import randint

async def rand_speaker(event: str) -> str:
    '''event: 需要随机的事件内容'''

    return f'吼后! {event}的概率是{str(randint(1, 99))}%哒!'