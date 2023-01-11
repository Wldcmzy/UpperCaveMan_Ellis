# 山顶洞人Ellis

# 描述

一个基于nonebot2的简单qqbot(但是nb2版本好久没更新了)

![sample01](README/sample01.png)

# 当前功能

附带链接的均为三方插件(部分有改动)，否则为自制

## 帮助

查看帮助菜单

## 权限测试

测试群以及超级用户权限

## 随机数生成

xx的概率是xxx(好玩)

## 查天气

~~查中华万年历~~
万年历g了， 现在爬中国气象局

每日三次推送

## 简单CV

已半重置 基本CV功能包括：反转图片，反转一半图片，变灰度图，二值化，滤波，canny边缘检测。参数固定，灵活性不高。

## 备忘录

基于sqlite3，预留用户权限判断接口，但是现在即使是几句话也懒得敲。

可定时推送

## 扫雷

基于opencv, 由于之前写了自治版就不想装公开插件了，功能比公开插件要弱一些

## 定时吵吵消息

按时烦人

## 简单数学运算

gcd，lcm，快速幂，exgcd，逆元（exgcd / 费马小定理），素数判断

## 复读判官

判断复读打断，或复读结束后总结复读

特性：现在不会打断超级用户、管理员、群主的腿了。

## 疯狂星期四

生成关于v我多少请我吃疯狂星期四的段子

插件链接：[MinatoAquaCrews/nonebot_plugin_crazy_thursday: Crazy Thursday plugin for nonebot2 beta & alpha from nonebot_instant_plugins (github.com)](https://github.com/MinatoAquaCrews/nonebot_plugin_crazy_thursday)

## 运势

今日运势与二次元图组合

插件链接：[MinatoAquaCrews/nonebot_plugin_fortune: Fortune divination plugin for nonebot2 beta from nonebot_instant_plugins (github.com)](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune)

## 制作头像相关的表情包

有很多类型

插件链接：[noneplugin/nonebot-plugin-petpet: Nonebot2 插件，用于制作摸头等头像相关表情包 (github.com)](https://github.com/noneplugin/nonebot-plugin-petpet)

## 随机唐可可

你能找到唐可可在哪吗？

插件链接：[MinatoAquaCrews/nonebot_plugin_randomtkk: Find Tan Kuku for nonebot2 beta from nonebot_instant_plugins (github.com)](https://github.com/MinatoAquaCrews/nonebot_plugin_randomtkk)

## 60秒读懂世界

这里是蔚蓝群？

每日推送

插件链接：[bingganhe123/60s-: 定时向指定群或列表好友发送每日60s读世界 (github.com)](https://github.com/bingganhe123/60s-)

## 人生重开模拟器

长大我要当太空人...

插件链接：[noneplugin/nonebot-plugin-remake: 适用于 Nonebot2 的人生重开模拟器 (github.com)](https://github.com/noneplugin/nonebot-plugin-remake)

## 历史上的今天

历史上的今天发生过哪些事呢？

每日推送

插件链接：[AquamarineCyan/nonebot-plugin-today-in-history: nonebot2历史上的今天 (github.com)](https://github.com/AquamarineCyan/nonebot-plugin-today-in-history)

## Wordle

没有人不喜欢玩wordle，如果有，就再来一道。

插件链接：[noneplugin/nonebot-plugin-wordle: Nonebot2 wordle猜单词插件 (github.com)](https://github.com/Wldcmzy/UpperCaveMan_Ellis/tree/ellis_rework/uppercaveman_ellis/plugins/nonebot_plugin_wordle)

## 塔罗牌

destiny...

插件链接：[MinatoAquaCrews/nonebot_plugin_tarot: Tarot divination plugin for nonebot2 beta from nonebot_instatnt_plugins (github.com)](https://github.com/MinatoAquaCrews/nonebot_plugin_tarot)

## 让机器人撤回消息

如题

插件链接：[noneplugin/nonebot-plugin-withdraw: A simple withdraw plugin for Nonebot2 (github.com)](https://github.com/noneplugin/nonebot-plugin-withdraw)

## 查看服务器状态[超管]

查看cpu，内存，磁盘，开机时间

插件链接：[QQ-GitHub-Bot/src/plugins/nonebot_plugin_status at master · cscs181/QQ-GitHub-Bot · GitHub](https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status)

## bilibili链接解析

插件链接：[mengshouer/nonebot_plugin_analysis_bilibili: nonebot2解析bilibili插件 (github.com)](https://github.com/mengshouer/nonebot_plugin_analysis_bilibili)

## 语句抽象化

插件链接： [CherryCherries/nonebot-plugin-abstract: 适用于 Nonebot2 的语句抽象化插件 (github.com)](https://github.com/CherryCherries/nonebot-plugin-abstract)



# 关于.dev文件

由于牵扯一些隐私信息就不放了, 文件格式大概像这样(不定期更新)

```
ENVIRONMENT=dev

SUPERUSERS=["777777777"]  # 配置 NoneBot 超级用户
NICKNAME=["山顶洞人", "Ellis", ",", "，"]  # 配置机器人的昵称
COMMAND_START=[""]  # 配置命令起始字符
COMMAND_SEP=[" "]  # 配置命令分割字符

#nonebot-plugin-read-60s
#nonebot-plugin-today-in-history
daily_qq_friends=[] #设定要发送的QQ好友
daily_qq_groups=[] #设定要发送的群
daily_inform_time=[{"hour":7,"minute":30}] 
#在输入时间的时候 不要 以0开>头如{"HOUR":06,"MINUTE":08}是错误的

#Ellis-weather
weather_qq_friends=[] #设定要发送的QQ好友 {"qq": xxx "city" : xxx}
weather_qq_groups=[{"CODE" : 7777777, "CITY" : "城市"},{"CODE":78777777,"CITY":"城市"}, {"CODE" : 666666, "CITY" : "城市"}] #设定要发送的群
weather_inform_time=[{"HOUR":6,"MINUTE":0},{"HOUR":12,"MINUTE":0},{"HOUR":17,"MINUTE":30}]
#在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的

# nonebot-plugin-imageutils
default_fallback_fonts = ["Arial", "Tahoma", "Helvetica Neue", "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", "Source Han Sans SC", "Noto Sans SC", "Noto Sans CJK JP", "WenQuanYi Micro Hei", "Apple Color Emoji", "Noto Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol"]


# Ellis-repeat-judger
repeat_judger_group = [89488989787789] # 可以使用复读判官的群(默认复读结束说话)
repeat_judger_group_interrupt = [456456464,22312312313, 56465456464564] # 机器人主动打断复读而非结束说话的群
repeat_judge_threshold = 3 # 判定复读的阈值 默认3
repeat_judge_threshold_random_add = 2 # 打断功能的判定复读阈值为随机数, 最多在原来的基础上加上这个值 默认0, 结束说话功能不受影响

#Ellis-noise
noise_qq_friends = [] # 定时发送吵吵消息的人
noise_qq_groups=[456456464,22312312313, 56465456464564] #定时发送吵吵消息的群

#Ellis-memo
memo_qq_groups = [456456464,22312312313, 56465456464564] # 定时发送备忘录消息的群
memo_inform_time = [{"hour":5,"minute":20}]

# nonebot-plugin-today-in-history
history_qq_friends=[] #设定要发送的QQ好友
history_qq_groups=[456456464,22312312313, 56465456464564] #设定要发送的群
history_inform_time="7 35" #设定每天发送时间，以空格间隔
```



# 额外说明

**仅供学习使用**
**不接受捐赠**

