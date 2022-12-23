from jieba import posseg
import requests
import json
import time
from nonebot.log import logger
from pathlib import Path
import pickle

stations_file: Path = Path(__file__).parent / "resource" / "stations.silksINFn"
with open(stations_file, 'rb') as f:
    DIC: dict[str, str] = pickle.load(f)

#===========================
#万年历g乐， 这个方法弃用乐
#===========================
#
# async def get_weather(pos : str) -> str:
#     header = {
#         "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#         "Accept-Encoding": "gzip, deflate",
#         "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
#         "Cache-Control": "max-age=0",
#         "Host": "wthrcdn.etouch.cn",
#         "Proxy-Connection": "keep-alive",
#         "Upgrade-Insecure-Requests": "1",
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.50",
#     }

#     '''pos : 中国地区名'''
#     if len(pos) <= 0:
#         return '我一介莽夫, 你让我猜你想查哪?'
#     try:
#         res = requests.get('http://wthrcdn.etouch.cn/weather_mini?city=%s' % pos, headers=header)
#         res = json.loads(res.text)
#         a = res['data']['forecast'][0]
#         tm = time.localtime()[ : 6]
#         ret = '本山顶洞人Ellis于公元%d年%d月%d日%d时%d分%d秒为您查询了中华万年历:\n' % tuple((tm[i] for i in range(6)))
#         ret += '地区 : %s\n' % pos
#         ret += '今天是' + a['date'] + '\n'
#         ret += a['high'] + ' ' + a['low'] + '\n'
#         ret += '天气为: ' + a['type'] + '\n'
#         ret += '风向为: ' + a['fengxiang'] + '\n'
#         ret += '风力为: ' + a['fengli'].replace('<![CDATA[', '').replace(']]>', '') + '\n'
#         if '雨' in a['type']:
#             ret += '\n记得带伞~\n'
#         elif '雪' in a['type']:
#             ret += '\n注意安全~\n'
#         elif '云' in a['type']:
#             ret += '\n软绵绵的云~\n'
#         else:
#             ret += '\n加油, 奥里给!\n'
#     except Exception as e:
#         ret = '呜呜呜~ 出错了\n:' + str(type(e)) + str(e) + f'\n中华万年历里有这个地方吗?\n地点:{pos}'
#     return ret 


async def get_weather(pos : str) -> str:
    if len(pos) <= 0: return '我一介莽夫, 你让我猜你想查哪?'
    if pos not in DIC: return '我不造啊!'
    code = DIC[pos]
    res = requests.get(f'http://www.weather.com.cn/data/sk/{code}.html')
    data = json.loads(res.content.decode('utf-8'))['weatherinfo']
    res = requests.get(f'http://www.weather.com.cn/data/cityinfo/{code}.html')
    data2 = json.loads(res.content.decode('utf-8'))['weatherinfo']
    ret = f'''
城市:{data2["city"]}
天气:{data2["weather"]}
温度:{data2["temp1"]} ~ {data2["temp2"]}
以下为实时数据:
采集时间:{data["time"]}
温度:{data["temp"]}
相对湿度:{data["SD"]}
风向:{data["WD"]}
风力:{data["WS"]}
气压:{data["AP"]}
Radar:{data["Radar"]}
isRadar:{data["isRadar"]}
    '''.strip()

    return ret
 

async def find_city(text : str) -> str:
    text = text.replace('天气', '').replace(' ', '')

    words, city = posseg.lcut(text), None
    for each in words:
        # logger.debug(each.word + ' ' + each.flag)
        if each.flag == 'ns':
            city = each.word
            break

    # 分词有时不准确, 这部分代码可以再一定程度上稍微补救, 但是经不起折腾
    if city == None: 
        for each in words:
            if len(each.word) <= 1: continue
            tail = each.word[-1]
            if tail in ['市', '区', '县']:
                city = each.word
                break       
        
    if city == None: city = text

    return city