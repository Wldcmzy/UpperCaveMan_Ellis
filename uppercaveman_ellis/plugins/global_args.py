# 可以玩扫雷的群
ClearMine_groups = {    
    793832002, # 火火火/洞口骑士死路求生
    904494576, # 光之国
    770769550, # steam特色喜加一
}
# 扫雷图片路径
ClearMine_pic_path = {
    'src' : 'uppercaveman_ellis/source/clearmind/', # 图源路径
    'out' : '../../nonebot/usr/local/bin/data/images/', # 输出图路径(对应go-cqhttp图片路径)
}


# 定时自动发送天气信息的群
Weather_autosend_groups_dic = {
    793832002 : '莱山', # 火火火/洞口骑士死路求生
    904494576 : '莱山', # 光之国
    770769550 : '寒亭', # steam特色喜加一
}

# 定时自动发生吵吵信息的群
Noise_autosend_groups = {
    793832002, # 火火火/洞口骑士死路求生
    904494576, # 光之国
    770769550, # steam特色喜加一
}

# 可以玩随机数的群
Rand_groups = {
    793832002, # 火火火/洞口骑士死路求生
    904494576, # 光之国
    770769550, # steam特色喜加一
}

# 复读判官插件参数
Repeat_judger_args_dic = {
    # 拥有复读判官插件权限的群
    'privilege' : {
        793832002, # 火火火/洞口骑士死路求生
        904494576, # 光之国
        770769550, # steam特色喜加一
        871127578, # 水水水
    },

    # 某群复读次数达到此阈值后, 认为此群正在复读
    'threshold' : 3,

    # 复读会被机器人打断的群
    'interrupt_group' : {
        871127578, # 水水水
    },
    # 复读被终止后,会提醒是谁终结了复读的群, 若群会被打断复读, 此项无效
    'whisper_group' : {
        793832002, # 火火火/洞口骑士死路求生
        904494576, # 光之国
        770769550, # steam特色喜加一
        871127578, # 水水水
    },
}

Memorandum_groups_users = {
    793832002 : { # 火火火/洞口骑士死路求生
        'allow_owner' : False,
        'allow_admin' : False,
        'allow_users' : {
            3457922487,
        },
    },
}