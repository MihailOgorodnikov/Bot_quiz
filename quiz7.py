import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from markup import markup1, markup2, markup5, markup6, markup7, markup8


def quiz7(dp: Dispatcher, bot: Bot):

    class Points(StatesGroup):
        name = State()
        advertising = State()
        furniture = State()
        equipment = State()
        acquiring = State()
        working = State()
        stock = State()
        landing = State()
        cockroaches = State()
        planogram = State()
        framework = State()
        uniform = State()
        plan = State()
        motivation = State()
        dynamics = State()
        checks = State()
        recalculation = State()
        compliance = State()
        discipline = State()
        desserts = State()
        storage = State()
        drink = State()
        qualitatively = State()
        check = State()
        corner = State()
        yandex = State()

    @dp.message_handler(text='Выставление баллов')
    async def cmd_start(message: types.Message):
        await message.answer("Ставим только баллы!", reply_markup=markup2)
        await message.answer("Напишите название кофейни:")
        await Points.name.set()


    @dp.message_handler(state=Points.name)
    async def process_name(message: types.Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer("1.Наружные рекламные конструкции:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.advertising)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(advertising=message.text)
        await message.answer("2.Мебель и торговое оборудование:")
        await message.answer("Бал 5 или 0?", reply_markup=markup6)
        await Points.next()

    @dp.message_handler(state=Points.furniture)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(furniture=message.text)
        await message.answer("3.Рекламное оборудование:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.equipment)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(equipment=message.text)
        await message.answer("4.Касса, экваринг:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.acquiring)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(acquiring=message.text)
        await message.answer("5.Рабочая зона бариста:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.working)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(working=message.text)
        await message.answer("6.Подсобное помещение:")
        await message.answer("Бал 3 или 0?", reply_markup=markup8)
        await Points.next()

    @dp.message_handler(state=Points.stock)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(stock=message.text)
        await message.answer("7.Зона посадки посетителей:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.landing)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(landing=message.text)
        await message.answer("8.В кофейне отсутствуют тараканы:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.cockroaches)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(cockroaches=message.text)
        await message.answer("9.Весь товар выставлен:")
        await message.answer("Бал 5 или 0?", reply_markup=markup6)
        await Points.next()

    @dp.message_handler(state=Points.planogram)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(planogram=message.text)
        await message.answer("10.Все ценники в наличии:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.framework)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(framework=message.text)
        await message.answer("11.Униформа утвержденная:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.uniform)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(uniform=message.text)
        await message.answer("12.Дневной план:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.plan)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(plan=message.text)
        await message.answer("13.мотивация бариста:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.motivation)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(motivation=message.text)
        await message.answer("14.динамика выполнения:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.dynamics)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(dynamics=message.text)
        await message.answer("15.КЗ проверки:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.checks)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(checks=message.text)
        await message.answer("16.Пересчет денег в Кассе:")
        await message.answer("Бал 5 или 0?", reply_markup=markup6)
        await Points.next()

    @dp.message_handler(state=Points.recalculation)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(recalculation=message.text)
        await message.answer("17.Соблюдение штатного расписания:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.compliance)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(compliance=message.text)
        await message.answer("18.Бариста соблюдает кассовую дисциплину:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.discipline)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(discipline=message.text)
        await message.answer("19.Десерты:")
        await message.answer("Бал 5 или 0?", reply_markup=markup6)
        await Points.next()

    @dp.message_handler(state=Points.desserts)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(desserts=message.text)
        await message.answer("20.Отсутствуют продукты с истекшим сроком хранения:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.storage)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(storage=message.text)
        await message.answer("21.Приготовленный напиток выглядел презентабельно:")
        await message.answer("Бал 4 или 0?", reply_markup=markup7)
        await Points.next()

    @dp.message_handler(state=Points.drink)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(drink=message.text)
        await message.answer("22.Сотрудники качественно работают со всей очередью:")
        await message.answer("Бал 4 или 0?")
        await Points.next()

    @dp.message_handler(state=Points.qualitatively)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(qualitatively=message.text)
        await message.answer("23.Сотрудники работают по чек листу кофейни:")
        await message.answer("Бал 5 или 0?", reply_markup=markup6)
        await Points.next()

    @dp.message_handler(state=Points.check)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(check=message.text)
        await message.answer("24.Уголок потребителя содержится в чистоте:")
        await message.answer("Бал 3 или 0?", reply_markup=markup8)
        await Points.next()


    @dp.message_handler(state=Points.corner)
    async def process_gender(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['corner'] = message.text

            await bot.send_message(
                message.chat.id,
                md.text(
                    md.text('Название кофейни:', data['name']),
                    md.text('1.Наружные рекламные конструкции:', data['advertising']),
                    md.text('2.Мебель и торговое оборудование:', data['furniture']),
                    md.text('3.Рекламное оборудование:', data['equipment']),
                    md.text('4.Касса, экваринг:', data['acquiring']),
                    md.text('5.Рабочая зона бариста:', data['working']),
                    md.text('6.Подсобное помещение:', data['stock']),
                    md.text('7.Зона посадки посетителей:', data['landing']),
                    md.text('8.В кофейне отсутствуют тараканы:', data['cockroaches']),
                    md.text('9.Весь товар выставлен:', data['planogram']),
                    md.text('10.Все ценники в наличии:', data['framework']),
                    md.text('11.Униформа утвержденная:', data['uniform']),
                    md.text('12.Дневной план:', data['plan']),
                    md.text('13.мотивация бариста:', data['motivation']),
                    md.text('14.динамика выполнения:', data['dynamics']),
                    md.text('15.КЗ проверки:', data['checks']),
                    md.text('16.Пересчет денег в Кассе:', data['recalculation']),
                    md.text('17.Соблюдение штатного расписания:', data['compliance']),
                    md.text('18.Бариста соблюдает кассовую дисциплину:', data['discipline']),
                    md.text('19.Десерты:', data['desserts']),
                    md.text('20.Отсутствуют продукты с истекшим сроком хранения:', data['storage']),
                    md.text('21.Приготовленный напиток выглядел презентабельно:', data['drink']),
                    md.text('22.Сотрудники качественно работают со всей очередью:', data['qualitatively']),
                    md.text('23.Сотрудники работают по чек листу кофейни:', data['check']),
                    md.text('24.Уголок потребителя содержится в чистоте:', data['corner']),
                    md.text('25.Общий балл кофейни:',
                            int(data['advertising']) +
                            int(data['furniture']) +
                            int(data['equipment']) +
                            int(data['acquiring']) +
                            int(data['working']) +
                            int(data['stock']) +
                            int(data['landing']) +
                            int(data['cockroaches']) +
                            int(data['planogram']) +
                            int(data['framework']) +
                            int(data['uniform']) +
                            int(data['plan']) +
                            int(data['motivation']) +
                            int(data['dynamics']) +
                            int(data['checks']) +
                            int(data['recalculation']) +
                            int(data['compliance']) +
                            int(data['discipline']) +
                            int(data['desserts']) +
                            int(data['storage']) +
                            int(data['drink']) +
                            int(data['qualitatively']) +
                            int(data['check']) +
                            int(data['corner'])),
                    sep='\n',
                ),
            )
        await message.answer("Вернулись в главное меню", reply_markup=markup5)
        await state.finish()