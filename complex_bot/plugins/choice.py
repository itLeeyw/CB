from nonebot import on_command,CommandSession
import random
import shlex
from nonebot import permission


@on_command('抽签', aliases=['专研', 'choice'], permission=permission.GROUP, only_to_me=False)
async def random_choice(session: CommandSession):
    argv = shlex.split(session.current_arg_text)
    if not argv:
        session.finish('谁是那个被选召的孩子')
    await session.send(random.choice(argv)+" !")
