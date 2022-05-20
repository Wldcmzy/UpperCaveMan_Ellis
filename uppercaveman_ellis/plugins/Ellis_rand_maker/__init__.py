from nonebot import on_command
from nonebot.adapters.onebot.v11 import Event, Message
from nonebot.params import CommandArg
from .source_data import rand_speaker
from .privilege import Role_rand

E_rand = on_command('rand ', aliases={'随机'}, rule=Role_rand)

@E_rand.handle()
async def E_rand_speaker(event : Event, args : Message = CommandArg()) -> None:    
    # plain_text = event.get_plaintext()
    plain_text = args.extract_plain_text()
    reply_text = await rand_speaker(plain_text)
    await E_rand.finish(reply_text)