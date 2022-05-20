import requests
import json
import time

async def get_weather(pos : str) -> str:
    '''中国地区名'''
    if len(pos) <= 0:
        return '我一介莽夫, 你让我猜你想查哪?'
    try:
        res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % pos)
        res = json.loads(res.text)
        a = res['data']['forecast'][0]
        tm = time.localtime()[ : 6]
        ret = '本山顶洞人Ellis于公元%d年%d月%d日%d时%d分%d秒为您查询了中华万年历:\n' % tuple((tm[i] for i in range(6)))
        ret += '地区 : %s\n' % pos
        ret += '今天是' + a['date'] + '\n'
        ret += a['high'] + ' ' + a['low'] + '\n'
        ret += '天气为: ' + a['type'] + '\n'
        ret += '风向为: ' + a['fengxiang'] + '\n'
        ret += '风力为: ' + a['fengli'].replace('<![CDATA[', '').replace(']]>', '') + '\n'
        if '雨' in a['type']:
            ret += '\n记得带伞~\n'
        elif '雪' in a['type']:
            ret += '\n注意安全~\n'
        elif '云' in a['type']:
            ret += '\n软绵绵的云~\n'
        else:
            ret += '\n加油, 奥里给!\n'
    except Exception as e:
        ret = '呜呜呜~\n出错了:' + str(e) + f'\n中华万年历里有这个地方吗?\n地点:{pos}'
    return ret 