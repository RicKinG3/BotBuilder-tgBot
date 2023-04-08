from aiogram import Bot
import logging

from core.settings import settings

async def onStartupNotify(bot: Bot):
    for admin in settings.bots.admins_id:
        try:
            chat = await bot.get_chat(admin)
            username = chat.username
            id = chat.id
            text = f"Hi admin {username} ({id}), i'm started and ready for work"
            await bot.send_message(chat_id=admin, text=text)
            # from  core.utils.commands import setCommands
            # await  setCommands(bot)

        except Exception as err:
            logging.exception(err)


async def onShutdownNotify(bot: Bot):
    for admin in settings.bots.admins_id:
        try:
            chat = await bot.get_chat(admin)
            username = chat.username
            id = chat.id

            text = f"bye {username} admin ({id}), i'm completed"
            await bot.send_message(chat_id=admin, text=text)
        except Exception as err:
            logging.exception(err)
