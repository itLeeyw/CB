from nonebot import on_command,CommandSession
from nonebot import permission as perm
import asyncio
from aiohttp import ClientSession
from nonebot import permission
from lxml import html
import re
etree = html.etree
import json
import pprint


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 \
    (KHTML,like Gecko) Chrome/62.0.3202.75 Safari/537.36"
}


@on_command('知乎日报', aliases=['今日日报', '今日新闻'], permission=permission.GROUP, only_to_me=False)
async def zhrb(session: CommandSession):
    url = 'https://news-at.zhihu.com/api/4/news/latest'
    STORY_URL = 'http://daily.zhihu.com/story/{}'
    async with ClientSession() as Csession:
        async with Csession.get(url) as response:
            r = await response.json()
            stories = r.get('top_stories')
            print(r.get)
            if not stories:
                await session.send("服务器爆炸了，你等哈子再专研")
                return
            else:
                rep = ''

                for story in stories:
                    surl = STORY_URL.format(story['id'])
                    title = story.get('title', "冒得内容")
                    rep += f'\n{title}\n{surl}\n'

                await session.send("今日知乎日报一览\n" + rep)






@on_command('开发者知识库', aliases=['问'], permission=permission.GROUP, only_to_me=False)#
async def kfzzsk(session: CommandSession):
    url = 'http://www.itdaan.com/so?q='
    async with ClientSession() as Csession:
        async with Csession.get(url+session.current_arg) as response:
            r = await response.read()
            #解析HTMl为HTMLDom模型
            content = etree.HTML(r)
            href = content.xpath("//html/body/div/div/div/div/div/div/dt/a/@href")

            if not href:
                await session.send("服务器爆炸了，你等哈子再专研")
                return
            else:
                rep = ''
                title = ''
                for hr,i in zip(href,range(5)):
                    title = str(i+1) + ').' + session.current_arg
                    rep += f'\n{title}\n{hr}\n'

                await session.send("前五条知识库回答：\n" + rep)

@on_command('mdn', aliases=['MDN'], permission=permission.GROUP, only_to_me=False)#
async def kfzzsk(session: CommandSession):
    url = 'https://developer.mozilla.org/zh-CN/search?q='
    async with ClientSession() as Csession:
        async with Csession.get(url+session.current_arg) as response:
            r = await response.read()
            #解析HTMl为HTMLDom模型
            content = etree.HTML(r)
            href = content.xpath("//*[@id=\"search-form\"]/div[2]/div[1]/div[2]/ul/li/div/div/h4/a/@href")
            title = content.xpath("//*[@id=\"search-form\"]/div[2]/div[1]/div[2]/ul/li/div/div/h4/a/text()")
            print(href)
            print(title)
            if not href:
                await session.send("服务器爆炸了，你等哈子再专研")
                return
            else:
                rep = ''
                for hr,t,i in zip(href,title,range(5)):
                    rep += f'\n{t}\n{hr}\n'

                await session.send("前五条MDN回答：\n" + rep)



