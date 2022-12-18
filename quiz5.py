import logging
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from markup import markup3, markup10, markup8


def quiz5(dp: Dispatcher, bot: Bot):

    class Latte(StatesGroup):
        tempering = State()
        before = State()
        strait = State()
        action = State()
        pitcher = State()
        pair = State()
        nozzle = State()
        transmission = State()
        remainder = State()
        temperature = State()
        foam = State()
        drink = State()
        corresponds = State()
        observed = State()
        served = State()

    @dp.message_handler(text='Латте')
    async def cmd_start(message: types.Message):
        await message.answer("Правильная темперовка.", reply_markup=markup10)
        await message.answer("Балл 1 или 0?")
        await Latte.tempering.set()

    @dp.message_handler(state=Latte.tempering)
    async def process_name(message: types.Message, state: FSMContext):
        await state.update_data(tempering=message.text)
        await message.answer("Пролив перед приготовлением.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.before)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(before=message.text)
        await message.answer("Незамедлитьтельный пролив.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.strait)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(strait=message.text)
        await message.answer("Последовательность действий.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.action)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(action=message.text)
        await message.answer("Чистый питчер.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.pitcher)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(pitcher=message.text)
        await message.answer("Пропускание пара до.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.pair)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(pair=message.text)
        await message.answer("Чистая форсунка.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.nozzle)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(nozzle=message.text)
        await message.answer("Пропускание пара после.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.transmission)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(transmission=message.text)
        await message.answer("Приемлимый остаток.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.remainder)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(remainder=message.text)
        await message.answer("Приемлимая температура.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.temperature)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(temperature=message.text)
        await message.answer("Текстура пены.", reply_markup=markup8)
        await message.answer("Балл 3 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.foam)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(foam=message.text)
        await message.answer("Обьем напитка соответствует.", reply_markup=markup10)
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.drink)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(drink=message.text)
        await message.answer("Вкус соответствует.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()

    @dp.message_handler(state=Latte.corresponds)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(corresponds=message.text)
        await message.answer("Рецептура соблюдена.")
        await message.answer("Балл 1 или 0?")
        await Latte.next()


    @dp.message_handler(state=Latte.observed)
    async def process_gender(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['observed'] = message.text

            await bot.send_message(
                message.chat.id,
                md.text(
                    md.text('Итоговый бал по напитку из 16:',
                            int(data['tempering']) +
                            int(data['before']) +
                            int(data['strait']) +
                            int(data['action']) +
                            int(data['pitcher']) +
                            int(data['pair']) +
                            int(data['nozzle']) +
                            int(data['transmission']) +
                            int(data['remainder']) +
                            int(data['temperature']) +
                            int(data['foam']) +
                            int(data['drink']) +
                            int(data['corresponds']) +
                            int(data['observed'])),
                    sep='\n',
                ),
            )
        await message.answer("Вернулись к практике бариста", reply_markup=markup3)
        await state.finish()
