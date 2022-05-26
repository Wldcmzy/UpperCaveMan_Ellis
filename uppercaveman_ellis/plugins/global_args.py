# 优先级
PRIORITY_RESPONSE_CD = 5
PRIORITY_NORMAL = 30
PRIORITY_PASSIVE = 60

# 响应消息冷却时间
PerUser_Response_CD = 1.5

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

# 轻量备忘录权限参数,群号写在这里面的群才有资格使用备忘录
# 默认拥有SUPERUSER权限的用户可以操作[所有][有备忘录权限的]群的备忘录
# 'allow_owner' : 允许群主操作开关
# 'allow_owner' : 允许管理员操作开关
# 'allow_users' : 允许操作本群备忘录的群成员集合
Memorandum_groups_users = {
    793832002 : { # 火火火/洞口骑士死路求生
        'allow_owner' : False,
        'allow_admin' : False,
        'allow_users' : {
            3457922487, # Ai-予人以爱
            1139198820, # tqc
            1527148777, # xxy
            1416995841, # rxj
        },
    },
    871127578 : { # 水水水
        'allow_owner' : False,
        'allow_admin' : False,
        'allow_users' : {
            
        }
    },
    904494576 : { # 光之国
        'allow_owner' : True,
        'allow_admin' : True,
        'allow_users' : {
            
        }
    }
}
Memorandum_data_path = '../Ellis_hide_source/memorandum_data/'

# 可以使用CV简单操作图片的群
CV_groups = {
    793832002, # 火火火/洞口骑士死路求生
    904494576, # 光之国
    770769550, # steam特色喜加一
    871127578, # 水水水
}

# CV图片路径
CV_pic_path = {
    'src' : '../Ellis_hide_source/CV_download/', # 图源(下载)路径
    'out' : '../../nonebot/usr/local/bin/data/images/CVtemp/', # 输出图路径(对应go-cqhttp图片路径)
    'extra' : 'CVtemp/', # out中images后面的路径
}

# CV库处理图片默认大小, 画质等
CV_pic_arg = {
    'default_long_edge' : 200,
    'jpg_qulity' : 90
}