from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from aiogram.types import InlineKeyboardButton, KeyboardButton, KeyboardButtonPollType, KeyboardButtonRequestUser, \
    KeyboardButtonRequestChat


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
    name_subject = ['Кнопки как шаблоны', 'Отреагировать на кнопку', 'Keyboard Builder', 'Специальные обычные кнопки',
                    'Назад']
    name_subject_en = ['BtnPatern', 'btnReact', 'KeyboardBuilder', 'SpecialRegularButtons', 'back_to_less_btn']

    buttons = InlineKeyboardBuilder()

    for i in range(len(name_subject)):
        buttons.add(InlineKeyboardButton(text=f"{name_subject[i]}", callback_data=f"{name_subject_en[i]}"))

    buttons.adjust(2)
    return buttons.as_markup()


def specialregkb():
    btn = ['Отправка геолокации', 'Отправка контакта с номером тел', 'Создания опроса/викторины',
           'Выбора и отправки боту данных пользователя с нужными критериями',
           'выбора и отправки боту данных (супер)группы или канала с нужными критериями',
           'запуска веб-приложения (WebApp)', 'Назад']
    return InlineKeyboardBuilder().add(
        *[InlineKeyboardButton(text=value, callback_data=f'super_btn{count}') for
          count, value in
          enumerate(btn)]).adjust(1).as_markup()


def example_get_geolocation():
    get_loc = ReplyKeyboardBuilder()
    get_loc.add(KeyboardButton(text="Запросить геолокацию", request_location=True))
    get_loc.add(KeyboardButton(text="Ловля геолокация через фильт", callback_data="print_filt_geolocation"))
    get_loc.add(KeyboardButton(text="Назад к меню", callback_data="back_to_main_menu"))

    return get_loc.adjust(1).as_markup(resize_keyboard=True, one_time_keyboard=False,
                                       input_field_placeholder="Выберете кнопку", selective=True)


def example_get_contact():
    get_contact = ReplyKeyboardBuilder()
    get_contact.add(KeyboardButton(text="Запросить контакт", request_contact=True))
    get_contact.add(KeyboardButton(text="Ловля контакта через фильт"))
    get_contact.add(KeyboardButton(text="Назад к меню", callback_data="back_to_main_menu"))

    return get_contact.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False,
                                           input_field_placeholder="Выберете кнопку", selective=True)


def example_quiz():
    get_quiz = ReplyKeyboardBuilder()
    get_quiz.add(KeyboardButton(text="Создать викторину", request_poll=KeyboardButtonPollType(type="quiz")))
    get_quiz.add(KeyboardButton(text="Назад к меню", callback_data="back_to_main_menu"))
    return get_quiz.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False,
                                        input_field_placeholder="Выберете кнопку", selective=True)


def example_get_bot_inf():
    get_bot_inf = ReplyKeyboardBuilder()

    get_bot_inf.add(KeyboardButton(text="Выбрать премиум пользователя",
                                   request_user=KeyboardButtonRequestUser(
                                       request_id=1,
                                       user_is_premium=True
                                   )))
    get_bot_inf.add(
        KeyboardButton(text="Прием выбора премиум пользователя", callback_data="Прием выбора премиум пользователя"))

    get_bot_inf.add(KeyboardButton(text="Назад к меню", callback_data="back_to_main_menu"))
    return get_bot_inf.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False,
                                           input_field_placeholder="Выберете кнопку", selective=True)


def example_get_user_categor():
    get_bot_inf = ReplyKeyboardBuilder()

    get_bot_inf.add(KeyboardButton(text="Выбрать супергруппу с форумами",
                                   request_chat=KeyboardButtonRequestChat(
                                       request_id=2,
                                       chat_is_channel=False,
                                       chat_is_forum=True
                                   )))
    get_bot_inf.add(
        KeyboardButton(text="Прием супергруппы с форумами", callback_data="Прием супергруппы с форумами"))

    get_bot_inf.add(KeyboardButton(text="Назад к меню", callback_data="back_to_main_menu"))
    return get_bot_inf.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False,
                                           input_field_placeholder="Выберете кнопку", selective=True)
