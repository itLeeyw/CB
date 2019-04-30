from nonebot import on_command,CommandSession
from nonebot import permission
import re


@on_command('计算', aliases=['算数'])
async def _(session: CommandSession):
    try:
        c = re.compile(r'amp;')
        formula = re.sub(c, '', session.current_arg)
        print("?111111111111111111"+formula)
        # 逆波兰表示法(后缀表示法)
        await session.send("答案 "+str(eval(formula)))
    except:
        await session.send("亲亲这边见你您输入正常的表达式呢")

