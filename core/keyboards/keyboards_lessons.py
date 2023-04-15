from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, KeyboardButton


def lessonsBackKb():
    back = ReplyKeyboardBuilder()
    back.add(KeyboardButton(text="Назад", callback_data="back_to_less"))

    back.adjust(1)
    return back.as_markup(resize_keyboard=True, one_time_keyboard=True,
                          input_field_placeholder="Выберете кнопку", selective=True)


def buttonsKb():
    name_subject = ['Обычные кнопки', 'Инлайн-кнопки', 'Назад']
    name_subject_en = ['ReplyKeyboard', 'InlineKeyboards', 'back_to_less']

    buttons = InlineKeyboardBuilder()

    for i in range(len(name_subject)):
        buttons.add(InlineKeyboardButton(text=f"{name_subject[i]}", callback_data=f"{name_subject_en[i]}"))

    buttons.adjust(2)
    return buttons.as_markup()


def replyInlineKb():
    name_subject = ['Кнопки как шаблоны',  'Отреагировать на кнопку', 'Keyboard Builder', 'Специальные обычные кнопки', 'Назад']
    name_subject_en = ['BtnPatern', 'react', 'KeyboardBuilder', 'SpecialRegularButtons', 'back_to_less_btn']

    buttons = InlineKeyboardBuilder()

    for i in range(len(name_subject)):
        buttons.add(InlineKeyboardButton(text=f"{name_subject[i]}", callback_data=f"{name_subject_en[i]}"))


    buttons.adjust(2)
    return buttons.as_markup()
