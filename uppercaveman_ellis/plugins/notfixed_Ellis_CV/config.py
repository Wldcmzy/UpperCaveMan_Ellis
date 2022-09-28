import time

PRIORITY_NORMAL = 15

# 可以使用CV简单操作图片的群
CV_groups = {
    793832002, 
    904494576, 
    770769550, 
    871127578, 
}

# CV图片路径
CV_pic_path = {
    'src' : './resource/src/', # 图源(下载)路径
    'out' : './resource/out/', # 输出图路径(对应go-cqhttp图片路径)
    'extra' : '../../../UpperCaveMan_Ellis/uppercaveman_ellis/plugins/resource/out/', # cqhttp读图路径
}

# CV库处理图片默认大小, 画质等
CV_pic_arg = {
    'default_long_edge' : 200,
    'jpg_qulity' : 90
}

def form_time_string(start = 0, end = 4):
    ret = ''
    for each in time.localtime()[start : end]:
        ret += str(each)
    return ret