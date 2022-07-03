Default_Mod = 998244353

def int_size_ensure(func, mod : int = Default_Mod):
    return lambda *args: func(*tuple(int(each) % mod for each in args))

def try_except_ensure(func):
    def new_func(*args):
        try:
            return func(*args)
        except Exception as e:
            async def __(e : Exception, *args) -> str: 
                return f'出错了:{type(e)}\n{str(e)}'
            return __(e, *args)
    return new_func

@try_except_ensure
@int_size_ensure
async def gcd(a : int, b : int) -> int:
    '''求a和b的最大公因数'''
    return a if not b else await gcd(b, a % b)

@try_except_ensure
@int_size_ensure
async def lcm(a : int, b : int) -> int:
    '''求a和b的最小公倍数'''
    return a // await gcd(a, b) * b

@try_except_ensure
@int_size_ensure
async def power(x : int, p : int, mod : int = Default_Mod) -> int:
    '''求x的p次幂%mod'''
    base, ans = x, 1
    while p >= 1:
        if p & 1: ans = ans * base % mod
        base = base ** 2 % mod
        p >>= 1
    return ans

@try_except_ensure
@int_size_ensure
async def exgcd(a : int, b : int) -> int:
    '''扩展欧几里得'''
    if b == 0: return 1, 0, a
    x, y, ret = await exgcd(b, a % b)
    return y, (x - (a // b) * y), ret

@try_except_ensure
@int_size_ensure
async def inverse_Fermat(x : int, p : int) -> int:
    '''求xmodp的逆元, 费马小定理, 只给答案, 不验证数据合法性'''
    return await power(x, p - 2, p)

@try_except_ensure
@int_size_ensure
async def inverse_exgcd(x : int, p : int) -> int:
    '''求xmodp的逆元, 扩展欧几里得'''
    x, y, ret = await exgcd(x, p)
    return x % p if ret == 1 else -0x7fffffff

@try_except_ensure
@int_size_ensure
async def isprime(x : int) -> bool:
    '''判断x是否为素数'''
    if x <= 1: return False
    for i in range(2, int(x ** 0.5) + 1):
        if not x % i: 
            return False
    return True

