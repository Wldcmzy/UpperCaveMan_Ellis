##############################################
# 一开始没用nb2而是手撸socket
# 这个扫雷是根据当时手撸socket版本改的
# 有些地方代码规则不是很到位
##############################################

from ctypes import Union
import numpy as np
import random
import cv2
from pathlib import Path
from nonebot.adapters.onebot.v11 import MessageSegment, Message

ClearMine_img_path: Path = Path(__file__).parent / "resource/image"
ClearMine_out_path: Path = Path(__file__).parent / "resource/out"

class ClearMine:
    dir = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    def __init__(
        self, 
        groupID : str,
        sz : int = 8, 
        num : int = 6, 
        path : Path = ClearMine_img_path, 
        outpath  : Path = ClearMine_out_path
        ) -> None:
        '''
        初始化
        sz : 雷区大小(sz x sz) 
        num : 雷的数量  
        path : 图源路径  
        outpath : 输出图路径
        '''
        self.cfg(sz, num)
        self.__MINE = 0x7fffffff
        self.__BOOM = 0x7ffffffe
        self.__path = path
        self.__outpath = outpath
        self.__outpicname = 'clearmindpic' + groupID + '.jpg'

    
    def cfg(self, sz : int, num : int) -> None:
        '''
        改变雷区配置,并重开游戏
        不合法数据会造成游戏bug, 应该在调用此方法前做好预处理
        一般此方法不直接调用, 而是通过parseOP方法调用
        sz : 雷区大小(sz x sz) 
        num : 雷的数量
        '''
        self.__num = num
        self.__sz = sz
        self.initialBoard()

    def initialBoard(self) -> None:
        '''初始化雷区'''
        self.__board = np.zeros([self.__sz + 1, self.__sz + 1], dtype = np.int32)
        self.__mask = np.zeros([self.__sz + 1, self.__sz + 1], dtype = np.int32)
        self.__start = False
        self.__count = 0

    def judgeEdge(self, x : int, y : int) -> bool:
        '''检查一个坐标是否在雷区内'''
        return x >= 1 and x <= self.__sz and y >= 1 and y <= self.__sz

    def putMine(self, x : int, y : int) -> None:
        '''
        开局第一次点击触发, 放置地雷
        x, y 表示点击坐标, 不会在这个坐标生成雷
        '''
        lst = list(range(1, self.__sz * self.__sz + 1))
        lst.remove((x - 1) * self.__sz + y)
        while len(lst) > self.__num:
            rd = random.randint(0, len(lst) - 1)
            del lst[rd]
            
        for each in lst:
            x = (each - 1) // self.__sz + 1
            y = each - ((x - 1) * self.__sz)
            self.__board[x][y] = self.__MINE
            for dx, dy in ClearMine.dir:
                xx, yy = x + dx, y + dy
                if self.judgeEdge(xx, yy) == False: continue
                if self.__board[xx][yy] == self.__MINE: continue
                self.__board[xx][yy] += 1

    def updateMask(self, x : int, y : int, click : bool = True) -> None:
        '''
        扫雷dfs函数
        click=True表示本轮dfs为dfs树树根
        '''
        if self.__mask[x][y] == 0:
            self.__mask[x][y] = 1
            self.__count += 1
        if self.__board[x][y] == 0:
            for each in ClearMine.dir:
                xx, yy = x + each[0], y + each[1]
                if self.judgeEdge(xx, yy) == False: continue
                if self.__mask[xx][yy] == 0:
                    self.updateMask(xx, yy, False)
        elif click == True:
            for each in ClearMine.dir:
                xx, yy = x + each[0], y + each[1]
                if self.judgeEdge(xx, yy) == False: continue
                if self.__mask[xx][yy] == 0 and self.__board[xx][yy] == 0:
                    self.updateMask(xx, yy, False)

    def selectCell(self, x : int, y : int) -> bool:
        '''模拟用户点击一个格子, 若点到雷返回False,否则返回True'''
        if self.__start == False: 
            self.__start = True
            self.putMine(x, y)
        if self.__board[x][y] == self.__MINE:
            self.__board[x][y] = self.__BOOM
            return False
        self.updateMask(x, y)
        return True

    def drawBoard(self, hasMask : bool = True) -> None:
        '''
        保存雷区图像到输出目录
        hasMask : 输出时是否考虑遮罩
        '''
        img = [cv2.imread(str(self.__path / f'C{str(i)}.png'), 1) for i in range(9)]
        mine = cv2.imread(str(self.__path / 'CMine.png'), 1)
        boom = cv2.imread(str(self.__path / 'CBoom.png'), 1)
        img.append(cv2.imread(str(self.__path / 'CMask.png'), 1))
        row = []
        for i in range(1, self.__sz + 1):
            col = None
            for j in range(1, self.__sz + 1):
                if hasMask == True and self.__mask[i][j] == 0:
                    col = img[-1] if j == 1 else np.column_stack((col, img[-1]))
                else:
                    if j != 1:
                        if self.__board[i][j] == self.__MINE:
                            col = np.column_stack((col, mine))
                        elif self.__board[i][j] == self.__BOOM:
                            col = np.column_stack((col, boom))
                        else:
                            col = np.column_stack((col, img[self.__board[i][j]]))
                    else:
                        if self.__board[i][j] == self.__MINE:
                            col = mine
                        elif self.__board[i][j] == self.__BOOM:
                            col = boom
                        else:
                            col = img[self.__board[i][j]]
            row.append(col)

        ret = np.row_stack(row)

        cv2.imwrite(str(self.__outpath / self.__outpicname), ret, [int(cv2.IMWRITE_JPEG_QUALITY),75])

    def foolishAI(self, x : int, y : int) -> Message:
        '''对用户输入以及扫雷结果做简单判断, 返回雷区图像以及文字提示'''
        ret = ''
        if self.judgeEdge(x, y) == False: return Message('扫出雷区了')
        if self.__mask[x][y] != 0: return Message(f'({x},{y})位置的状况已经知道了, 不需要再扫了')
        if self.selectCell(x, y) == False:
            ret += '雷炸了, 你怎么回事?\n' if random.randint(1, 100) <= 50 else '雷炸了, 你个垃圾!\n'
            ret += '游戏自动重启~\n'
            self.drawBoard(False)
            self.initialBoard()
        else:
            if self.__count >= (self.__sz ** 2) - self.__num:
                self.drawBoard(False)
                ret += '\n恭喜你完成扫雷, 游戏会自动重开~'
                self.initialBoard()
            else:
                ret = f'({x},{y})位置扫描完成\n'
                self.drawBoard()

        img = MessageSegment.image(f'file://{self.__outpath / self.__outpicname}')
        return Message(ret).append(img)
        
    def parseOP(self, args: list[str], mode : str = 'click') -> Message:
        '''解析用户输入的参数, 执行响应命令'''
        ret = ''
        try:
            if mode == 'cfg':
                sz, num = int(args[0]), int(args[1])
                if sz <=0 or num <= 0:
                    return Message('李载赣砷魔?')
                if sz > 15:
                    return Message('场地太大了, 你的眼睛受得了吗?\n(打死不加行列标)')
                if num >= sz * sz:
                    return Message('智商和你, 总有一个有问题...')
                self.cfg(sz, num)
                ret = Message('已经将扫雷参数设置为: 场地大小%dx%d, %d个雷\n游戏自动重启~' % (sz, sz, num))
            elif mode == 'show':
                self.drawBoard()
                ret = Message().append(MessageSegment.image(f'file://{self.__outpath / self.__outpicname}'))
            elif mode == 'click':
                x, y = int(args[0]), int(args[1])
                ret = self.foolishAI(x, y)
        except Exception as e:
            ret = f'出错蜡! {type(e)}|{str(e)}'
        return ret