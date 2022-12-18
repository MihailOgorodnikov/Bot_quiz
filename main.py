import logging
import os

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext
from aiogram.utils import executor
import quiz1
import quiz2
from markup import markup1

logging.basicConfig(level=logging.INFO)

API_TOKEN = os.environ['API_TOKEN']

bot = Bot(token=API_TOKEN)

storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='Отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    logging.info('Cancelling state %r', current_state)
    await state.finish()
    await message.answer("Вернулись в главное меню", reply_markup=markup1)

@dp.message_handler(text='Назад')
async def cmd_start(message: types.Message):
    await message.answer("Вернулись назад", reply_markup=markup1)

quiz1.quiz1(dp, bot)
quiz2.quiz2(dp, bot)

@dp.message_handler(commands=['start'])
async def process_hi4_command(message: types.Message):
    await message.answer("Добро пожаловать в бота", reply_markup=markup1)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
