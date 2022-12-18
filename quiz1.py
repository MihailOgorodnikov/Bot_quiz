import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from markup import markup1, markup2, markup5
import quiz6
import quiz7


def quiz1(dp: Dispatcher, bot: Bot):

    @dp.message_handler(text='Проверка кофейни')
    async def cmd_start(message: types.Message):
        await message.answer("Проверка кофейни", reply_markup=markup5)

    quiz6.quiz6(dp, bot)
    quiz7.quiz7(dp, bot)