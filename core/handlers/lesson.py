from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from core.keyboards.keyboards_lessons import buttons_kb
from core.keyboards.keyboards_main import lessons_kb, main_back_kb

router = Router()

@router.message(Text("Уроки"))
async def startBtn(message: Message):
    await message.answer(" вы",
                         reply_markup=main_back_kb())
    await message.answer("Отличное время для бота! надеюсь я смогу тебе помочь",
                         reply_markup=lessons_kb())



@router.callback_query(Text("back_to_less"))
async def lessMessage(callback: CallbackQuery):
    await callback.message.answer("Назад к урокам!", reply_markup=lessons_kb())

@router.callback_query(Text("less_1"))
async def lessMessage(callback: CallbackQuery):
    await callback.message.answer("1")

# Кнопки
@router.callback_query(Text("less_2"))
async def lessBtn(callback: CallbackQuery):
    await callback.message.answer("Вы попали на урок по кнопкам!", reply_markup=buttons_kb())


@router.callback_query(Text("less_3"))
async def lessRouter(callback: CallbackQuery):
    await callback.message.answer("3")

@router.callback_query(Text("less_4"))
async def lessFilter(callback: CallbackQuery):
    await callback.message.answer("4")