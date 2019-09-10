import  requests
from  t_getHoney import getHoney
import  re
import  time
import aiohttp
import asyncio
import  datetime

async def get_media_id(user_id):
    base_url = f'http://m.toutiao.com/profile/{user_id}/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, headers=headers) as response:
            if response.status == 200:
                text = await response.text()
                media_id = re.search('data-mediaid="(.*?)"', text).group(1)
                if media_id:
                    return media_id

async def get_data(user_id, max_behot=0):
    base_url = 'https://www.toutiao.com/pgc/ma/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Referer': f'http://m.toutiao.com/profile/{user_id}/'
               }
    media_id = await get_media_id(user_id)
    count = 0
    while True:
        _as,_cp = getHoney()
        params = {
            "page_type": "1",
            "max_behot_time": f"{max_behot}",
            "uid": f"{user_id}",
            "media_id": f"{media_id}",
            "output": "json",
            "is_json": "1",
            "count": "20",
            "from": "user_profile_app",
            "version": "2",
            "as": f"{_as}",
            "cp": f"{_cp}"
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(base_url, params=params, headers=headers) as response:
                if response.status == 200:
                    data = await response.json()
                    max_behot = data['next']['max_behot_time']
                    has_more = data['has_more']
                    if len(data['data']) > 1:
                        for item  in data['data']:
                            title = item['title']
                            url = item['url']
                            go_detail_count = item['go_detail_count']
                            print(title)
                            print(url)
                            print(go_detail_count,'\n')
                            count += 1
                        print(count, user_id)
                    if not has_more:
                        break
        time.sleep(1)



start =  datetime.datetime.now()
loop = asyncio.get_event_loop()
tasks = [get_data(14861272888), get_data(2892047273)]
loop.run_until_complete(asyncio.wait(tasks))
print((datetime.datetime.now()-start).total_seconds())
