from nonebot import on_command,CommandSession
from nonebot import permission

@on_command('命令大全',aliases=['所有命令','allcmd'], permission=permission.GROUP, only_to_me=False)
async def _(session: CommandSession):
    await session.send("/ || >> || ''命令 + 操作 使用" + "\n" 
                                              "命令大全\n"\
                                              "---------娱乐---------\n"\
                                              "知乎日报\n掷骰子\n专研\n\n"\
                                              "---------专研---------\n"\
                                              "你好(test用例)\n" \
                                              "计算\n" \
                                              "开发者知识库\n" \
                                              "MDN\n" \
                                              "翻译\n" \
                                              "a或者lt\n\n" \
                                              "/*\n*a为沙雕bot在线聊天,后续功能正在开发\n*Gakki是李伟豪老婆\n*"
            )
@on_command('李伟豪',aliases=['李伟豪是谁'],permission=permission.GROUP,only_to_me=False)
async def _(session: CommandSession):
    await session.send("李伟豪是Gakki的...")