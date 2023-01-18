import requests
from urllib import parse
from bs4 import BeautifulSoup
from bs4.element import NavigableString, Tag
from typing import Optional, Union
from nonebot.log import logger

_headers={
    'user-agent':'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.55',
    'Connection': 'keep-alive'
}

def recode(s: str) -> str:
    return parse.quote(s)

def judge404(s: str) -> bool:
    return s.startswith('https://baike.baidu.com/error.html?status=404')

def judgeHua(s: str) -> bool:
    return s.startswith('https://baike.baidu.com/anticrawl/captchaview')

def judgeNone(s: str) -> bool:
    return s == None

def query(thing: str) -> tuple[int, str, Optional[list[Tag]]]:
    '''
    第一个返回值:
        -4: 404
        -3: 滑块验证
        -2: 意料之外的错误
        -1: 无描述
        0: 正常
    '''
    global _headers

    try:

        url = f'https://baike.baidu.com/item/' + recode(thing)
        res = requests.get(url, headers = _headers)

        if judge404(res.url): 
            return -4, '未找到相应页面,可能此词条百度百科未收录', None
        
        if judgeHua(res.url):
            logger.warning(f'>>>>>>>>>>>>>>> baike滑块验证:{res.url}')
            return -3, f'滑块验证', None

        soup = BeautifulSoup(res.text, 'lxml')
        description = soup.find('meta', attrs={'name' : 'description'})

        if judgeNone(description):
            return -1, '未提取到描述', None

        description = description['content']
        ret = description

        lies = soup.find('ul', attrs={'class' : 'polysemantList-wrapper cmn-clearfix'})
        if not judgeNone(lies):
            lies = lies.find_all('li')

            ret += '\n\n输入序号查看其他可能的释义:\n'
            for i, each in enumerate(lies):
                if each.a != None:
                    ret += f'{str(i + 1)}. {each.a.string}\n'

        return 0, ret, lies

    except Exception as e:
        return -2, f'意料之外的错误  {type(e)} | {str(e)}', None

def query_directly(tag: Tag) -> tuple[int, str]:
    '''
    第一个返回值:
        -4: 404
        -3: 滑块验证
        -2: 意料之外的错误
        -1: 无描述
        0: 正常
    '''
    global _headers
    try:

        url = f'https://baike.baidu.com' + tag.a['href']
        res = requests.get(url, headers = _headers)

        if judge404(res.url): 
            return -4, '未找到相应页面,可能此词条百度百科未收录'
        
        if judgeHua(res.url):
            return -3, f'滑块验证'

        soup = BeautifulSoup(res.text, 'lxml')
        description = soup.find('meta', attrs={'name' : 'description'})

        if judgeNone(description):
            return -1, '未提取到描述'
        
        
        description = description['content']

        return 0, description
    
    except Exception as e:
        return -2, f'意料之外的错误 {type(e)} | {str(e)}'


if __name__ == '__main__':
    def verify():
        x, y, z = query('猪')
        print(x)
        print(y)
        print(z)
    
    # verify()

    
