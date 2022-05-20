

async def Help_tip() -> str:
    ret = '=>=>=>=>=[帮助界面]=<=<=<=<=\n'
    ret += '\n'
    ret += '=>=>[注意]<=<=\n'
    ret += '对于不同的人、群、命令可能都有不同的使用权限制\n'
    ret += '\n'
    ret += '=>=>[术语释意以及其他说明]<=<=\n'
    ret += '定向命令:必须要@机器人或在句首说明机器人昵称才可以触发命令\n'
    ret += '机器人昵称有:`,` `，` `山顶洞人` `Ellis`\n'
    ret += '关键词检测:检测到关键词就可以触发的命令, 若不是, 只能首部匹配\n'
    ret += '命令:执行某命令需要的文本\n'
    ret += '完全匹配:命令并除空字符外没有其他任何信息才能触发\n'
    ret += '\n'
    ret += '=>=>[帮助界面]<=<=\n'
    ret += '定向命令:否, 关键词检测:否, 完全匹配:是\n'
    ret += '命令: `帮助`, `help`\n'
    ret += '功能1: 命令(查询帮助界面)\n'
    ret += '\n'
    ret += '=>=>[天气]<=<=\n'
    ret += '定向命令:否, 关键词检测:否, 完全匹配:否\n'
    ret += '命令: `天气`\n'
    ret += '功能1: 命令+地点(用于查询天气)\n'
    ret += '\n'
    ret += '=>=>[随机数]<=<=\n'
    ret += '定向命令:否, 关键词检测:否, 完全匹配:否\n'
    ret += '命令: `rand` `随机`\n'
    ret += '功能1: 命令+语句(为此语句描述的事物随机一个1-99的概率)\n'
    ret += '\n'
    ret += '=>=>[扫雷]<=<=\n'
    ret += '定向命令:否, 关键词检测:否, 完全匹配:否\n'
    ret += '命令: `扫雷` `clearmine` `clearmind` `明镜止水之心`\n'
    ret += '功能1: 如: 命令 5 5(扫坐标为[5, 5]的雷)\n'
    ret += '功能2: 如: 命令 cfg 9 7(重置游戏为雷区大小9x9,有7个雷)\n'
    ret += '功能3: 如: 命令 查看(查看目前雷区的状态)\n'

    return ret