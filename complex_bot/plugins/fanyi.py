from nonebot import on_command,CommandSession
from nonebot import permission
import time
import requests
import hashlib
from aiohttp import ClientSession

@on_command('fanyi', aliases=['翻译','fy'],permission=permission.GROUP,only_to_me=False)
async def fy(session: CommandSession):
    d = session.current_arg
    m = hashlib.md5()
    u = 'fanyideskweb'  #判断是网页还是客户端
    # 由于网页是用的js的时间戳(毫秒)跟python(秒)的时间戳不在一个级别，所以需要*1000
    f = str(int(time.time()*1000))
    c = "rY0D^0'nM0}g5Mm1z%1G4"
    #根据md5的方式：md5(u + d + f + c)，拼接字符串生成sign参数。
    m.update((u + d + f + c).encode('utf-8'))   #生成加密串
    data= {
        'i':d,
        'from':'AUTO',
        'to':'AUTO',            #判断是自动翻译还是人工翻译
        'smartresult':'dict',
        'client':u,
        'salt':f,               #当前时间戳
        'sign':m.hexdigest(),   #获取加密串
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION', #判断按回车提交或者点击按钮提交的方式
        'typoResult':'true'
    }

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Origin':'http://fanyi.youdao.com/',  #请求头最初是从youdao发起的，Origin只用于post请求
        'Referer':'http://fanyi.youdao.com/', #Referer则用于所有类型的请求
    }
    #print(data)
    #接口
    post = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom='
    async with ClientSession() as Csession:
        async with Csession.post(post, headers=headers, data=data) as response:
            youdaojson = await response.json()

    await session.send((youdaojson['translateResult'][0][0]['tgt']))

