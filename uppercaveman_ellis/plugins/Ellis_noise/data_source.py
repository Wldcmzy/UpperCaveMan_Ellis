from datetime import datetime

def kaoyan23():
    d1 = datetime.strptime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), '%Y-%m-%d %H:%M:%S')
    d2 = datetime.strptime('2022-12-24 00:00:00', '%Y-%m-%d %H:%M:%S')
    return f'8点乐, 洗脸刷牙出去卷乐~\n23考研还剩{str((d2 - d1).days)}天乐~'