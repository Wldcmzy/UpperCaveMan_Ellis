HELP_help = '''help or 帮助
[帮助] - 打开帮助菜单
[petpet help] - 查看petpet表情包插件功能
'''

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

HELP_math = '''
少量数学运算,带[]的为可选参数
gcd a b
lcm a b
pow x p [mod] (快速幂)
ispirme x
inv (待重置) (求逆元)
'''.strip()

HELP_tarot = '''塔罗牌
占卜：[占卜]；
得到单张塔罗牌回应：[塔罗牌]；
[超管] 开启/关闭群聊转发模式：[开启|启用|关闭|禁用] 群聊转发模式，可降低风控风险。
'''.strip()

HELP_withdraw = ''',撤回 (当机器人犯错，群友可以将其撤回)
需要指定跟机器人说才行，示例：
[@机器人 撤回] # 撤回倒数第一条消息
[, 撤回 1]    # 撤回倒数第二条消息
[山顶洞人 撤回 0-3] # 撤回倒数三条消息
[Ellis 撤回 2-5]    # 撤回倒数第3-倒数第5条消息
区间左闭右开，序号从0开始
'''.strip()

HELP_status = '''戳一戳
查看服务器状态[超管]
'''.strip()

HELP_bilibili_analyze = '''
bilibili链接解析
发送bilibili链接或分析, 自动解析其介绍
'''

ALL_HELP_LIST = [
    HELP_help,
    HELP_wordle, 
    HELP_today_in_history, 
    HELP_random_tkk, 
    HELP_crazy_thursday,
    HELP_remake,
    HELP_fortune,
    HELP_weather,
    HELP_test_privilege,
    HELP_rand,
    HELP_math,
    HELP_tarot,
    HELP_withdraw,
    HELP_status,
    HELP_bilibili_analyze,
]

async def Help_tip() -> list:
    return_list = []    
    text = ''
    for each in ALL_HELP_LIST:
        text += f'=>{each}\n\n'
        if len(text) > 768:
            return_list.append(text)
            text = ''
            
    if text != '': return_list.append(text)
    return return_list