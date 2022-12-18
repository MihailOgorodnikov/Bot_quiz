import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from markup import markup10, markup9, markup3


def quiz3(dp: Dispatcher, bot: Bot):

    class Espresso(StatesGroup):
        Coefficient = State()
        filter = State()
        dosage = State()
        tempering = State()
        before = State()
        strait = State()
        action = State()
        corresponds = State()
        observed = State()

    @dp.message_handler(text='Эспрессо')
    async def cmd_start(message: types.Message):
        await message.answer("Коэфициент заваривания.", reply_markup=markup9)
        await message.answer("Балл 2 или 0?")
        await Espresso.Coefficient.set()

    @dp.message_handler(state=Espresso.Coefficient)
    async def process_name(message: types.Message, state: FSMContext):
        await state.update_data(Coefficient=message.text)
        await message.answer("Чистый фильтр.", reply_markup=markup10)
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.filter)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(filter=message.text)
        await message.answer("Правильная дозировка кофе.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.dosage)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(dosage=message.text)
        await message.answer("Правильная темперовка.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.tempering)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(tempering=message.text)
        await message.answer("Пролив перед приготовлением.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.before)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(before=message.text)
        await message.answer("Незамедлитьтельный пролив.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.strait)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(strait=message.text)
        await message.answer("Последовательность действий.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.action)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(action=message.text)
        await message.answer("Вкус соответствует.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()

    @dp.message_handler(state=Espresso.corresponds)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(corresponds=message.text)
        await message.answer("Рецептура соблюдена.")
        await message.answer("Балл 1 или 0?")
        await Espresso.next()


    @dp.message_handler(state=Espresso.observed)
    async def process_gender(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['observed'] = message.text

            await bot.send_message(
                message.chat.id,
                md.text(
                    md.text('Итоговый бал по напитку из 10:',
                            int(data['Coefficient']) +
                            int(data['filter']) +
                            int(data['dosage']) +
                            int(data['tempering']) +
                            int(data['before']) +
                            int(data['strait']) +
                            int(data['action']) +
                            int(data['corresponds']) +
                            int(data['observed'])),
                    sep='\n',
                ),
            )
        await message.answer("Вернулись к практике бариста", reply_markup=markup3)
        await state.finish()
