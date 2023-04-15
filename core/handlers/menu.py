from aiogram.types import Message, CallbackQuery
from aiogram import Router
from aiogram.filters import Text

from core.keyboards.keyboards_main import start_kb

router = Router()


@router.message(Text("/start"))
async def startBtn(message: Message):
    await message.answer(
        f"Привет! Здесь ты можешь найти для себя полезную информацию для постройки бота и многое другое :)",
        reply_markup=start_kb())

@router.callback_query(Text("back_to_main_menu"))
async def goStartBtnInline(callback: CallbackQuery):
    await callback.message.answer("Назад к меню", reply_markup=start_kb())

@router.message(Text("Назад к меню"))
async def goStartBtn(message: Message):
    await message.answer(
        f"Привет! Здесь ты можешь найти для себя полезную информацию для постройки бота и многое другое :)",
        reply_markup=start_kb())
