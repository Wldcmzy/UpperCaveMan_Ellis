
HELP_wordle = '''wordle
可发送“结束”结束游戏；可发送“提示”查看提示
可使用 -l / --length 指定单词长度，默认为 5
可使用 -d / --dic 指定词典，默认为 CET4
支持的词典：GRE、考研、GMAT、专四、TOEFL、SAT、专八、IELTS、CET4、CET6
wordle [-l --length <length>] [-d --dic <dic>] [--hint] [--stop] [word]
'''.strip()

HELP_today_in_history = '''历史上的今天
'''.strip()

HELP_random_tkk = '''随机唐可可
开始游戏：[随机 + 唐可可/鲤鱼/鲤鱼王/Liyuu/liyuu]+[简单/普通/困难/地狱/自定义数量]
输入答案：[答案是][行][空格][列]，行列为具体数字，例如：答案是114 514；
答案正确则结束此次游戏；不正确则直至倒计时结束，Bot公布答案并结束游戏；
提前结束游戏：[找不到唐可可/唐可可人呢/呼叫鲤鱼姐]，仅游戏发起者可提前结束游戏；
'''.strip()

HELP_crazy_thursday = '''疯狂星期四
[疯狂星期X] 随机输出KFC疯狂星期四文案
[狂乱X曜日] 随机输出KFC疯狂星期四文案
'''.strip()

HELP_remake = '''人生重开
remake/liferestart/人生重开/人生重来
'''.strip()

HELP_fortune = '''运势
[今日运势/抽签/运势] 抽签
[指定xx签] 指定特殊角色签底，需要自己尝试哦~
[设置xx签] 设置群抽签主题
[重置抽签] 重置群抽签主题
[主题列表] 查看可选的抽签主题
[抽签设置] 查看群抽签主题
'''.strip()

HELP_weather = '''天气
关键词检测，需要附加中国地名
'''.strip()

HELP_test_privilege = '''权限测试or测试权限
'''.strip()

HELP_rand = '''rand 或者 随机
返回一个随机数(好玩)
'''.strip()

ALL_HELP_LIST = [
    HELP_wordle, 
    HELP_today_in_history, 
    HELP_random_tkk, 
    HELP_crazy_thursday,
    HELP_remake,
    HELP_fortune,
    HELP_weather,
    HELP_test_privilege,
    HELP_rand,
]

async def Help_tip() -> list:
    return_list = []    
    text = ''
    for each in ALL_HELP_LIST:
        text += f'=>{each}\n\n'
        if len(text) > 512:
            return_list.append(text)
            text = ''
            
    if text != '': return_list.append(text)
    return return_list