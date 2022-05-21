import numpy as np
import random
import cv2
from ..global_args import ClearMine_pic_path
from nonebot.log import logger

class ClearMine:
    dir = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
    def __init__(self, sz : int = 6, num : int = 8, path : str = ClearMine_pic_path['src'], outpath  : str = ClearMine_pic_path['out']) -> None:
        '''sz : 雷区大小(sz x sz) num : 雷的数量  path : 图源路径  outpath : 输出图路径'''
        self.cfg(sz, num)
        self.__MINE = 0x7fffffff
        self.__BOOM = 0x7ffffffe
        self.__path = path
        self.__outpath = outpath

    # 改变雷区配置,并重开游戏
    # 不合法数据会造成游戏bug, 此方法没有处理, 应该在外部做好判断
    # 一般此方法不直接调用, 而是通过parseOP方法调用
    def cfg(self, sz : int, num : int) -> None:
        '''sz : 雷区大小(sz x sz) num : 雷的数量'''
        self.__num = num
        self.__sz = sz
        self.initialBoard()

    # 初始化雷区
    def initialBoard(self) -> None:
        self.__board = np.zeros([self.__sz + 1, self.__sz + 1], dtype = np.int32)
        self.__mask = np.zeros([self.__sz + 1, self.__sz + 1], dtype = np.int32)
        self.__start = False
        self.__count = 0

    # 判断坐标是否越过边界 ([1 - sz] 闭区间)
    def judgeEdge(self, x : int, y : int) -> bool:
        return x >= 1 and x <= self.__sz and y >= 1 and y <= self.__sz

    # 开局第一次点击触发,放置地雷,参数位置永远不会放雷
    def putMine(self, x : int, y : int) -> None:
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

    # 通过DFS扫开遮罩
    def updateMask(self, x : int, y : int, click : bool = True) -> None:
        '''click表示是否首次点击,主动调用时,建议使用默认参数True'''
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

    # 模拟用户点击一个格子, 若点到雷返回False,否则返回True
    def selectCell(self, x : int, y : int) -> bool:
        if self.__start == False: 
            self.__start = True
            self.putMine(x, y)
        if self.__board[x][y] == self.__MINE:
            self.__board[x][y] = self.__BOOM
            return False
        self.updateMask(x, y)
        return True

    # 保存雷区图像,返回图片CQ码
    def outputBoard(self, hasMask : bool = True) -> str:
        '''hasMask : 输出时是否考虑遮罩'''
        img = [cv2.imread(self.__path + 'C' + str(i) + '.png', 1) for i in range(9)]
        mine = cv2.imread(self.__path + 'CMine.png', 1)
        boom = cv2.imread(self.__path + 'CBoom.png', 1)
        img.append(cv2.imread(self.__path + 'CMask.png', 1))
        row = []
        for i in range(1, self.__sz + 1):
            col = ''
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

        cv2.imwrite(self.__outpath + 'ClearMineReturnPic.jpg', ret, [int(cv2.IMWRITE_JPEG_QUALITY),50])
        return '[CQ:image,file=ClearMineReturnPic.jpg]'

    # 对用户输入以及扫雷结果做简单判断, 返回雷区图像以及文字提示
    def foolishAI(self, x : int, y : int) -> str:
        ret = ''
        if self.judgeEdge(x, y) == False: return '扫出雷区了'
        if self.__mask[x][y] != 0: return f'({x},{y})位置的状况已经知道了, 不需要再扫了'
        if self.selectCell(x, y) == False:
            ret += '雷炸了, 你怎么回事?\n' if random.randint(1, 100) <= 50 else '雷炸了, 你个垃圾!\n'
            ret += '游戏自动重启~\n'
            ret += self.outputBoard(False)
            self.initialBoard()
        else:
            if self.__count >= (self.__sz ** 2) - self.__num:
                ret = self.outputBoard(hasMask = False)
                ret += '\n恭喜你完成扫雷, 游戏会自动重开~'
                self.initialBoard()
            else:
                ret = f'({x},{y})位置扫描完成\n'
                ret += self.outputBoard()
        
        return ret
    
    # 解析用户输入的参数, 执行响应命令
    def parseOP(self, op : str) -> str:
        ret = ''
        try:
            if op[ : 3] == 'cfg':
                data = op.split()
                sz, num = int(data[1]), int(data[2])
                if sz <=0 or num <= 0:
                    return '李载赣砷魔?'
                if sz > 12:
                    return '场地太大了, 你的眼睛受得了吗?\n(打死不加行列标识)'
                if num >= sz * sz:
                    return '智商和你, 总有一个有问题...'
                self.cfg(sz, num)
                ret = '已经将扫雷参数设置为: 场地大小%dx%d, %d个雷\n游戏自动重启~' % (sz, sz, num)
            elif op[ : 2] == '查看':
                ret = self.outputBoard()
            else:
                data = op.split()
                x, y = int(data[0]), int(data[1])
                ret = self.foolishAI(x, y)
        except Exception as e:
            ret = '出错蜡! ' + str(e)
        return ret