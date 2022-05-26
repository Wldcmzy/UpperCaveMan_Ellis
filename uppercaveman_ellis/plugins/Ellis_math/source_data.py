def int_sure(x , mod : int = 998244353) -> int:
    return int(x) % mod

async def gcd(a : int, b : int) -> int:
    return a if b == 0 else await gcd(b, a % b)

async def lcm(a : int, b : int) -> int:
    return a // await gcd(a, b) * b

async def power(x : int, p : int, mod : int = 998244353) -> int:
    base, ans = x, 1
    while p >= 1:
        if p & 1: ans = ans * base % mod
        base = base ** 2 % mod
        p >>= 1
    return ans

async def exgcd(a : int, b : int) -> int:
    if b == 0: return 1, 0, a
    x, y, ret = await exgcd(b, a % b)
    return y, (x - (a // b) * y), ret

async def inverse_Fermat(x : int, p : int) -> int:
    return await power(x, p - 2, p)

async def inverse_exgcd(x : int, p : int) -> int:
    x, y, ret = await exgcd(x, p)
    return x % p if ret == 1 else -0x7fffffff

async def isprime(x : int):
    i, ret = 2, True
    while i * i <= x:
        if x % i == 0:
            ret = (False, i)
            break
        i += 1
    return ret


