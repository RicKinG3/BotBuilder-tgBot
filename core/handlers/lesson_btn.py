from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery
from aiogram import F

from core.keyboards.keyboards_lesson_btn import replyInlineKb, specialregkb, \
    example_get_geolocation, example_get_contact, example_quiz, example_get_bot_inf, example_get_user_categor

router = Router()


@router.callback_query(Text("ReplyKeyboard"))
async def lessRouter(callback: CallbackQuery):
    await callback.message.edit_reply_markup("Обычные кнопки", reply_markup=replyInlineKb())


@router.callback_query(Text("BtnPatern"))
async def lessRouterPatern(callback: CallbackQuery):
    await callback.message.answer("<b>Кнопки как шаблоны</b>")
    await callback.message.answer(
        "Для уменьшения кнопок к объекту клавиатуры надо указать дополнительный параметр resize_keyboard=True \n"
        "input_field_placeholder= доп параметр")

    await callback.message.answer(
        '<pre><code class="language-python">'  " kb_book_eval = ReplyKeyboardMarkup(keyboard=[ "  '</code></pre>'
        '<pre><code class="language-python">'  "     [ "  '</code></pre>'
        '<pre><code class="language-python">'  "         KeyboardButton(text='1) За все время'), "  '</code></pre>'
        '<pre><code class="language-python">'  "         KeyboardButton(text='2) За месяц'), "  '</code></pre>'
        '<pre><code class="language-python">'  "         KeyboardButton(text='3) За день'), "  '</code></pre>'
        '<pre><code class="language-python">'  "     ], "  '</code></pre>'
        '<pre><code class="language-python">'  "     [ "  '</code></pre>'
        '<pre><code class="language-python">'  "         KeyboardButton(text='/menu') "  '</code></pre>'
        '<pre><code class="language-python">'  "     ] "  '</code></pre>'
        '<pre><code class="language-python">'  "  "  '</code></pre>'
        '<pre><code class="language-python">'  " ], resize_keyboard=True)  # ЧТОБ КНОПКИ НЕ БЫЛИ НА ПОЛ ЭКРАНА "  '</code></pre>'

        '<pre><code class="language-python">'  " await message.answer(f'За какой промежуток времени показать рейтинг ?\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "     f'3) За день', reply_markup=kb_book_eval) "  '</code></pre>')
    await callback.message.answer(
        "Чтобы удалить кнопки, необходимо отправить новое сообщение со специальной «удаляющей» клавиатурой типа ReplyKeyboardRemove. Например: "
        '<pre><code class="language-python">'  "await message.reply(TEXT, reply_markup=types.ReplyKeyboardRemove()) " '</code></pre>')


@router.callback_query(Text("btnReact"))
async def lessRouterReact(callback: CallbackQuery):
    await callback.message.answer("<b>Реакция на нажатие кнопок</b>")
    await callback.message.answer('<pre><code class="language-python">'  " # новый импорт! "  '</code></pre>'
                                  '<pre><code class="language-python">'  " from aiogram.filters import Text "  '</code></pre>'
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  " @dp.message(Text(TEXT)) "  '</code></pre>'
                                  '<pre><code class="language-python">'  " async def with_puree(message: types.Message): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     await message.reply(TEXT) "  '</code></pre>'
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  " @dp.message(lambda message: message.text == TEXT) "  '</code></pre>'
                                  '<pre><code class="language-python">'  " async def without_puree(message: types.Message): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     await message.reply(TEXT) "  '</code></pre>')

    await callback.message.answer("Если через Роутеры @router")


@router.callback_query(Text("KeyboardBuilder"))
async def lessKeyboardBuilder(callback: CallbackQuery):
    await callback.message.answer(
        "<b>Для более динамической генерации кнопок можно воспользоваться сборщиком клавиатур. Нам пригодятся следующие методы:</b>")
    await callback.message.answer(
        '* add(<KeyboardButton>) — добавляет кнопку в память сборщика;\n'
        '* adjust(int1, int2, int3...) — делает строки по int1, int2, int3... кнопок; \n'
        '* as_markup() — возвращает готовый объект клавиатуры;\n'
        '* button(<params>) — добавляет кнопку с заданными параметрами, тип кнопки (Reply или Inline) определяется автоматически.',
        parse_mode=None)
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  " # новый импорт! "  '</code></pre>'
                                  '<pre><code class="language-python">'  " from aiogram.utils.keyboard import ReplyKeyboardBuilder "  '</code></pre>'
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  " def lessons_kb(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     less_name = ['Работа с сообщениями', 'Кнопки', 'Роутеры, структура', 'Фильтры', 'Назад'] "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     return InlineKeyboardBuilder().add(*[InlineKeyboardButton( "  '</code></pre>'
                                  '<pre><code class="language-python">'  "         text=Урок №{count} {value} , callback_data=less_callback[count-1]) for count, value in "  '</code></pre>'
                                  '<pre><code class="language-python">'  "         enumerate(less_name, start=1)]).adjust(2).as_markup() "  '</code></pre>')

    await callback.message.answer("""У объекта обычной клавиатуры есть ещё две полезных опции: 
    * one_time_keyboard для автоматического скрытия кнопок после нажатия 
    * selective для показа клавиатуры лишь некоторым участникам группы. 
    Их использование остаётся для самостоятельного изучения.""")


@router.callback_query(Text("SpecialRegularButtons"))
async def lessSpecialRegularButtons(callback: CallbackQuery):
    await callback.message.answer("Специальные обычные кнопки", reply_markup=specialregkb())


@router.callback_query(Text("super_btn0"))
async def specialBtnGeolocation(callback: CallbackQuery):
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  " def example_get_geolocation(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     return ReplyKeyboardBuilder().add(KeyboardButton(text = TEXT, request_location=True)).adjust( "  '</code></pre>'
                                  '<pre><code class="language-python">'  "         1).as_markup(resize_keyboard=True, one_time_keyboard=True, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                      input_field_placeholder=TEXT, selective=True) "  '</code></pre>'
                                  , reply_markup=example_get_geolocation())


@router.message(Text("Ловля геолокация через фильт"))
async def specialBtnGeolocation(message: Message):
    await message.answer(
        '<pre><code class="language-python">'  " @router.message(F.location) "  '</code></pre>'
        '<pre><code class="language-python">'  " async def getLocation(message: Message): "  '</code></pre>'
        '<pre><code class="language-python">'  "     location = message.location "  '</code></pre>'
        '<pre><code class="language-python">'  "     await message.reply(f'Твая геолокация: \n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Широта = {location.latitude}\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Долгота = {location.longitude}\n') "  '</code></pre>'
    )


@router.message(F.location)
async def getLocation(message: Message):
    location = message.location
    await message.reply(f'Твая геолокация: \n'
                        f'Широта = {location.latitude}\n'
                        f'Долгота = {location.longitude}\n')


@router.callback_query(Text("super_btn1"))
async def specialBtnGeolocation(callback: CallbackQuery):
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  " def example_get_contact(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_contact = ReplyKeyboardBuilder() "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_contact.add(KeyboardButton(text=TEXT, request_contact=True)) "  '</code></pre>'
                                  '<pre><code class="language-python">'  "      "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     return get_contact.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False, "  '</code></pre>'

                                  , reply_markup=example_get_contact())


@router.message(F.contact)
async def getLocation(message: Message):
    tel = message.contact
    await message.reply(f'Твой номер телефона: {tel.phone_number}\n'
                        f'Имя = {tel.first_name}\n'
                        f'Фамилия = {tel.last_name}\n'
                        f'Твой айди = {tel.user_id}\n'
                        f'Визитная карточка контакта в формате vCard 3.0  = {tel.vcard}')


@router.message(Text("Ловля контакта через фильт"))
async def specialBtnGeolocation(message: Message):
    await message.answer(
        '<pre><code class="language-python">'  " @router.message(F.contact) "  '</code></pre>'
        '<pre><code class="language-python">'  " async def getLocation(message: Message): "  '</code></pre>'
        '<pre><code class="language-python">'  "     tel = message.contact "  '</code></pre>'
        '<pre><code class="language-python">'  "     await message.reply(f'Твой номер телефона: {tel.phone_number}\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Имя = {tel.first_name}\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Фамилия = {tel.last_name}\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Твой айди = {tel.user_id}\n' "  '</code></pre>'
        '<pre><code class="language-python">'  "                         f'Визитная карточка контакта в формате vCard 3.0  = {tel.vcard}') "  '</code></pre>'

    )


@router.callback_query(Text("super_btn2"))
async def specialBtnGeolocation(callback: CallbackQuery):
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  " def example_quiz(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_contact = ReplyKeyboardBuilder() "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_contact.add(KeyboardButton(text=text, request_poll=KeyboardButtonPollType(type=QUIZ))) "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_contact.add(KeyboardButton(text=TEXT, callback_data=TEXT)) "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     return get_contact.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False, "  '</code></pre>'

                                  , reply_markup=example_quiz())


@router.callback_query(Text("super_btn3"))
async def specialBtnGeolocation(callback: CallbackQuery):
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  " def example_get_bot_inf(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_bot_inf = ReplyKeyboardBuilder() "  '</code></pre>'
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_bot_inf.add(KeyboardButton(text Текс, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                    request_user=KeyboardButtonRequestUser( "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                        request_id=1, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                        user_is_premium=True "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                    ))) "  '</code></pre>'

                                  , reply_markup=example_get_bot_inf())


@router.message(F.user_shared)
async def on_user_shared(message: Message):
    print(
        f"Request {message.user_shared.request_id}. "
        f"User ID: {message.user_shared.user_id}"
    )


@router.message(Text("Прием выбора премиум пользователя"))
async def getPremiumUser(message: Message):
    await message.answer('<pre><code class="language-python">'  " @router.message(F.user_shared) "  '</code></pre>'
                         '<pre><code class="language-python">'  " async def on_user_shared(message: Message): "  '</code></pre>'
                         '<pre><code class="language-python">'  "     print( "  '</code></pre>'
                         '<pre><code class="language-python">'  "       Request {message.user_shared.request_id}. "  '</code></pre>'
                         '<pre><code class="language-python">'  "       User ID: {message.user_shared.user_id}"   '</code></pre>'
                         '<pre><code class="language-python">'  "     ) "  '</code></pre>')


@router.callback_query(Text("super_btn4"))
async def specialBtnGeolocation(callback: CallbackQuery):
    await callback.message.answer("<b>Пример</b>"
                                  '<pre><code class="language-python">'  " def example_get_user_categor(): "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_bot_inf = ReplyKeyboardBuilder() "  '</code></pre>'
                                  '<pre><code class="language-python">'  "  "  '</code></pre>'
                                  '<pre><code class="language-python">'  "     get_bot_inf.add(KeyboardButton(text=, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                    request_chat=KeyboardButtonRequestChat( "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                        request_id=2, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                        chat_is_channel=False, "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                        chat_is_forum=True "  '</code></pre>'
                                  '<pre><code class="language-python">'  "                                    ))) "  '</code></pre>'

                                  '<pre><code class="language-python">'  "     return get_bot_inf.adjust(2).as_markup(resize_keyboard=True, one_time_keyboard=False, "  '</code></pre>'

                                  , reply_markup=example_get_user_categor())


@router.message(F.chat_shared)
async def on_user_shared(message: Message):
    print(
        f"Request {message.chat_shared.request_id}. "
        f"User ID: {message.chat_shared.chat_id}"
    )


@router.message(Text("Прием супергруппы с форумами"))
async def getPremiumUser(message: Message):
    await message.answer('<pre><code class="language-python">'  " @router.message(F.chat_shared) "  '</code></pre>'
                         '<pre><code class="language-python">'  " async def on_user_shared(message: Message): "  '</code></pre>'
                         '<pre><code class="language-python">'  "     print( "  '</code></pre>'
                         '<pre><code class="language-python">'  "         Request {message.chat_shared.request_id}.  "  '</code></pre>'
                         '<pre><code class="language-python">'  "         User ID: {message.chat_shared.chat_id}"  '</code></pre>'
                         '<pre><code class="language-python">'  "     ) "  '</code></pre>'
                         )
