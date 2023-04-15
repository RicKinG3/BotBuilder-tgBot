from aiogram import Router
from aiogram.filters import Text
from aiogram.types import Message, CallbackQuery

from core.keyboards.keyboards_lessons import buttonsKb, replyInlineKb, lessonsBackKb
from core.keyboards.keyboards_main import lessons_kb, main_back_kb

router = Router()

@router.message(Text("Уроки"))
async def startBtn(message: Message):
    await message.answer("Отличное время для бота!",
                         reply_markup=main_back_kb())
    await message.reply("Надеюсь я смогу тебе помочь",
                         reply_markup=lessons_kb())


@router.callback_query(Text("back_to_less"))
async def lessMessage(callback: CallbackQuery):
    await callback.message.edit_reply_markup("Назад к урокам!", reply_markup=lessons_kb())

@router.callback_query(Text("less_1"))
async def lessMessage(callback: CallbackQuery):
    await callback.message.answer("1")

# Кнопки
@router.callback_query(Text("less_2"))
async def lessBtn(callback: CallbackQuery):
    await callback.message.edit_reply_markup("Вы попали на урок по кнопкам!", reply_markup=buttonsKb())


@router.callback_query(Text("ReplyKeyboard"))
async def lessRouter(callback: CallbackQuery):
    await callback.message.edit_reply_markup("Обычные кнопки", reply_markup=replyInlineKb())

@router.callback_query(Text("BtnPatern"))
async def lessRouter(callback: CallbackQuery):
    await callback.message.answer("<b>Кнопки как шаблоны</b>")
    await callback.message.answer("Для уменьшения кнопок к объекту клавиатуры надо указать дополнительный параметр resize_keyboard=True \n"
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
                '<pre><code class="language-python">'  "await message.reply(TEXT, reply_markup=types.ReplyKeyboardRemove()) " '</code></pre>'  )


@router.callback_query(Text("back_to_less_btn"))
async def lessMessage(callback: CallbackQuery):
    await callback.message.edit_reply_markup("Назад к выбору кнопок!", reply_markup=buttonsKb())

@router.callback_query(Text("less_3"))
async def lessRouter(callback: CallbackQuery):
    await callback.message.answer("3")

@router.callback_query(Text("less_4"))
async def lessFilter(callback: CallbackQuery):
    await callback.message.answer("4")