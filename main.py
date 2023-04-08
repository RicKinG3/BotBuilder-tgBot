import asyncio
import logging
from aiogram import Bot, Dispatcher


async def start():
    logging.basicConfig(level=logging.INFO)

    from core.settings import settings
    bot = Bot(token=settings.bots.bot_token, parse_mode='HTML')

    dp = Dispatcher()

    from core.utils.notify_admins import onStartupNotify, onShutdownNotify
    dp.startup.register(onStartupNotify)
    dp.shutdown.register(onShutdownNotify)

    # мб вызов в хендлере  ???
    from core.utils.commands import commands
    await bot.set_my_commands(commands)

    from core.handlers import menu, lesson
    dp.include_routers(menu.router, lesson.router)

    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        await dp.stop_polling()
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(start())
