from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault

commands = [
    BotCommand(
        command='start',
        description='Запуск бота'
    ),
    BotCommand(
        command='help',
        description='Помощь'
    ),
    BotCommand(
        command='cancel',
        description='Сброс'
    ),
    BotCommand(
        command='man',
        description='Сброс'
    )
]
#
#
# async def setCommands(bot: Bot):
#     print("Asdsd")
#     commands = [
#         BotCommand(
#             command='start',
#             description='Запуск бота'
#         ),
#         BotCommand(
#             command='help',
#             description='Помощь'
#         ),
#         BotCommand(
#             command='cancel',
#             description='Сброс'
#         ),
#         BotCommand(
#             command='man',
#             description='Сброс'
#         )
#     ]
#
#     await bot.set_my_commands(commands, BotCommandScopeDefault())

#
# async def setAdminsCommand(bot: Bot, id_adm):
#     admins_commands = [
#         BotCommand(
#             command='admin',
#             description='only for admins'
#         )
#     ]
#
#
#     scope = BotCommandScopeChatAdministrators(chat_id=1982851211)
#     await bot.set_my_commands(commands=admins_commands,scope=scope)
