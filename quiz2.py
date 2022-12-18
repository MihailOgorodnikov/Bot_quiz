from aiogram import Bot, Dispatcher, types

import quiz3
import quiz4
import quiz5
from markup import markup3


def quiz2(dp: Dispatcher, bot: Bot):

    @dp.message_handler(text='Практика бариста')
    async def cmd_start(message: types.Message):
        await message.answer("Практика бариста ставим только баллы", reply_markup=markup3)

    quiz3.quiz3(dp, bot)
    quiz4.quiz4(dp, bot)
    quiz5.quiz5(dp, bot)



