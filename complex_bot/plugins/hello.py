from nonebot import on_command,CommandSession
from nonebot import permission


@on_command('你好', aliases=['你好强'], permission=permission.GROUP, only_to_me=False)
async def _(session: CommandSession):
    await session.send("哦")


@on_command('get_count', aliases=['群人数'], permission=permission.GROUP, only_to_me=False)
async def a(session: CommandSession):
    group_id = session.ctx['group_id']
    member_list = await session.bot.get_group_member_list(
        group_id=group_id
    )
    print(member_list)
    await session.send(f'群中共有{len(member_list)}个人')
