import aiohttp
import asyncio
import json
import pickle

SEMAPHORE = 8

async def get_provinces_code() -> dict[str, str]:
    URL = 'http://www.weather.com.cn/data/city3jdata/china.html'
    async with semaphore:
        async with session.get(URL) as res:
            return json.loads(await res.text())

async def get_cities_code(province_code: str) -> tuple[str, dict[str, str]]:
    URL = 'http://www.weather.com.cn/data/city3jdata/provshi/{}.html'.format(province_code)
    async with semaphore:
        async with session.get(URL) as res:
            return province_code, json.loads(await res.text())

async def get_stations_code(city_code: str) -> tuple[str, dict[str, str]]:
    URL = 'http://www.weather.com.cn/data/city3jdata/station/{}.html'.format(city_code)
    async with semaphore:
        async with session.get(URL) as res:
            return city_code, json.loads(await res.text())

async def query():
    global session, semaphore
    session = aiohttp.ClientSession()
    semaphore = asyncio.Semaphore(SEMAPHORE)

    provinces_dict: dict[str, str] = await get_provinces_code()

    tasks: list[asyncio.Task[tuple[str, dict[str, str]]]] = []
    for code, province in provinces_dict.items():
        tasks.append(asyncio.ensure_future(get_cities_code(code)))
    await asyncio.wait(tasks)

    lst: list[str] = []
    for task in tasks:
        province_code, cities_dict = task.result()
        for code, city in cities_dict.items():
            lst.append(province_code + code)

    tasks = [asyncio.ensure_future(get_stations_code(each)) for each in lst]
    await asyncio.wait(tasks)

    final_dict: dict[str, str] = {}
    for task in tasks:
        city_code, stations_dict = task.result()
        for code, station in stations_dict.items():
            final_dict[station] = city_code + code
    
    with open('stations.silksINFn', 'wb') as f:
        pickle.dump(final_dict, f)

def main():
    global loop

    loop = asyncio.get_event_loop()
    loop.run_until_complete(query())

    session.close()

if __name__ == '__main__':
    main()
