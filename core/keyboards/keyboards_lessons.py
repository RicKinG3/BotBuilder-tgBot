from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, KeyboardButton


def lessons_back_kb():
    back = ReplyKeyboardBuilder()
    back.add(KeyboardButton(text="Назад", callback_data="back_to_less"))

    back.adjust(1)
    return back.as_markup(resize_keyboard=True, one_time_keyboard=True,
                          input_field_placeholder="Выберете кнопку", selective=True)


def buttons_kb():
    name_subject = ['Обычные кнопки', 'Инлайн-кнопки', 'Назад']
    buttons = InlineKeyboardBuilder()

    number_subject: int = 1
    for i in name_subject:
        buttons.add(InlineKeyboardButton(text=f"{number_subject}", callback_data=f"less_{number_subject}"))
        number_subject += 1

    buttons.adjust(2)
    return buttons.as_markup()
