import sqlite3
from sqlite3 import Connection
from pathlib import Path
import datetime
from typing import Union

DB_PATH: Path = Path(__file__).parent / "resource"

def try_except_ensure(func):
    def new_func(*args) -> Union[str, list[str]]:
        try:
            return func(*args)
        except Exception as e:
            def __(e : Exception, *args) -> str: 
                return f'出错了:{type(e)}|{str(e)}'  
            return __(e, *args)
    return new_func

def open_table(path: Path) -> Connection:
    if not path.exists():
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE MEMO(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            DATA           TEXT     ,
            USER           TEXT     ,
            TIME           TEXT     );
        ''')
    else:
        conn = sqlite3.connect(path)

    return conn

@try_except_ensure
def memo_add(group_id: str, user_id: str, data: str) -> str:
    '''把数据存进数据库, 返回提示信息'''
    
    conn = open_table(DB_PATH / (group_id + '.db'))
    cursor = conn.cursor()

    nowtime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(f'''
        INSERT INTO MEMO (USER, TIME, DATA)
        VALUES ("{user_id}", "{nowtime}", "{data}");
    ''')

    conn.commit()
    conn.close()

    return '大概写好了~'

@try_except_ensure
def memo_see(group_id: str) -> list[str]:
    '''以字符串列表形式返回数据库信息'''
    conn = open_table(DB_PATH / (group_id + '.db'))
    cursor = conn.cursor()
    cursor.execute('''
        SELECT ID, USER, TIME, DATA
        from MEMO;
    ''')

    lst, text = [], ''
    for mid, userid, datatime, data in cursor.fetchall():
        print(mid, userid, datatime, data)
        text += f'{mid}. {data}\n 由{userid}于{datatime}写入\n'
        if len(text) >= 512:
            lst.append(text)
            text = ''
    if text != '': lst.append(text)
    conn.close()

    return lst

@try_except_ensure
def memo_del(group_id: str, index: str) -> str:
    conn = open_table(DB_PATH / (group_id + '.db'))
    cursor = conn.cursor()

    cursor.execute(f'''
        SELECT ID 
        FROM MEMO 
        WHERE ID = "{int(index)}";
    ''')
    if cursor.fetchall() == []:
        conn.close()
        return '序号错误~'

    cursor.execute(f'''
        DELETE 
        FROM MEMO
        WHERE ID = "{int(index)}";
    ''')
    conn.commit()
    conn.close()

    return '大概删了~'
