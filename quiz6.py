import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from markup import markup1, markup2, markup5


def quiz6(dp: Dispatcher, bot: Bot):

    class Comment(StatesGroup):
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

    @dp.message_handler(text='Проверка кофейни с коментариями')
    async def cmd_start(message: types.Message):
        await message.answer("Пишем ответы на вопросы")
        await message.answer("Название кофейни:", reply_markup=markup2)
        await Comment.name.set()


    @dp.message_handler(state=Comment.name)
    async def process_name(message: types.Message, state: FSMContext):
        await state.update_data(name=message.text)
        await message.answer("Наружные рекламные конструкции: вывеска, баннер, доп. рекламные элементы, Входная группа: дверь, крыльцо, перила, коврики, рольставни, урна, Фасад (стены, окна, витражи, крыша)?")
        await Comment.next()

    @dp.message_handler(state=Comment.advertising)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(advertising=message.text)
        await message.answer("Мебель и торговое оборудование (прилавок, витрины, куб, кофемашина, кофемолка, холодильники, микроволновка); Пол, стены, потолок, двери, подоконники и другие поверхности кофейни. Урна и контейнеры не переполнены.?")
        await Comment.next()

    @dp.message_handler(state=Comment.furniture)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(furniture=message.text)
        await message.answer("Рекламное оборудование/материалы (меню над прилавком, рекламные панно, монетницы, холдеры, рекламные наклейки)?")
        await Comment.next()

    @dp.message_handler(state=Comment.equipment)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(equipment=message.text)
        await message.answer("Касса, экваринг, Электрооборудование: (освещение, розетки, эл/щиток, проводка, кондиционер, тепловая завеса, обогреватели и т.п.), отсутствие посторонних запахов.?")
        await Comment.next()

    @dp.message_handler(state=Comment.acquiring)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(acquiring=message.text)
        await message.answer("Рабочая зона бариста?")
        await Comment.next()

    @dp.message_handler(state=Comment.working)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(working=message.text)
        await message.answer("Подсобное помещение, склад?")
        await Comment.next()

    @dp.message_handler(state=Comment.stock)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(stock=message.text)
        await message.answer("Зона посадки посетителей (чистота, целостность)?")
        await Comment.next()

    @dp.message_handler(state=Comment.landing)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(landing=message.text)
        await message.answer("В кофейне отсутствуют тараканы, мухи, грызуны (мухоловка в рабочем состоянии и установлена вдали от кухонных поверхностей)?")
        await Comment.next()

    @dp.message_handler(state=Comment.cockroaches)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(cockroaches=message.text)
        await message.answer("Весь товар выставлен в соответствии с планограммой кофейни?")
        await Comment.next()

    @dp.message_handler(state=Comment.planogram)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(planogram=message.text)
        await message.answer("Все ценники в наличии и актуальны. Рамки ценников чистые: пыль грязь и остатки клеевой основы отсутствуют?")
        await Comment.next()

    @dp.message_handler(state=Comment.framework)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(framework=message.text)
        await message.answer("Униформа утвержденная, чистая, не изношенная, Бейджи установленного образца с именами одеты на всех сотрудниках.Руки чистые. Ногти коротко подстрижены. У женщин маникюр, без страз, без блёсток?")
        await Comment.next()

    @dp.message_handler(state=Comment.uniform)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(uniform=message.text)
        await message.answer("Дневной план (знает да/нет) ТВ/Стаканы 0,6/0,4, знают прогноз выполнения?")
        await Comment.next()

    @dp.message_handler(state=Comment.plan)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(plan=message.text)
        await message.answer("Мотивация бариста (ставка  час/KPI/КЗ), умеют ли ее расчитывать?")
        await Comment.next()

    @dp.message_handler(state=Comment.motivation)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(motivation=message.text)
        await message.answer("Динамика выполнения (ТВ/Стаканы/%списания)?")
        await Comment.next()

    @dp.message_handler(state=Comment.dynamics)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(dynamics=message.text)
        await message.answer("КЗ проверки % мотивация (свой показатель)?")
        await Comment.next()

    @dp.message_handler(state=Comment.checks)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(checks=message.text)
        await message.answer("Пересчет денег в Кассе. В кофейне соблюдаются «Правила безопасности при работе с контрольно – кассовой машиной Инкассация сдается ежедневно?")
        await Comment.next()

    @dp.message_handler(state=Comment.recalculation)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(recalculation=message.text)
        await message.answer("Соблюдение штатного расписания, Медицинские книжки персонала в наличи. Если медицинская книжка находится на оформлении или продлении, то должен быть предоставлен документ (чек об оплате/справка) подтверждающий данную процедуру?")
        await Comment.next()

    @dp.message_handler(state=Comment.compliance)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(compliance=message.text)
        await message.answer("Бариста соблюдает кассовую дисциплину работает быстро: выполняет правило: сначала оплата, затем выдача напитков; обязательное закрытие стола и денежного ящика; выдача чека гостю обязательно?")
        await Comment.next()

    @dp.message_handler(state=Comment.discipline)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(discipline=message.text)
        await message.answer("Десерты при выкладке на витрину маркируются датой выкладки и датой достижения предельного срока?")
        await Comment.next()

    @dp.message_handler(state=Comment.desserts)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(desserts=message.text)
        await message.answer("Отсутствуют продукты с истекшим сроком хранения. Списанные продукты категории выпечка хранятся на полке, обозначенной: для списания или в упаковке с маркировкой списание?")
        await Comment.next()

    @dp.message_handler(state=Comment.storage)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(storage=message.text)
        await message.answer("Приготовленный напиток выглядел презентабельно, стакан без подтеков. Выдавая напиток, бариста поблагодарил гостя или доброжелательно попрощался с ним?")
        await Comment.next()

    @dp.message_handler(state=Comment.drink)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(drink=message.text)
        await message.answer("Сотрудники качественно работают со всей очередью: устанавливают зрительный контакт, приветствуют, всем уделяют внимание, никто из гостей не уходит (общее время обслуживания гостя от момента входа, до получения напитка не более 5 минут с момента того, как гость встал в очередь)?")
        await Comment.next()

    @dp.message_handler(state=Comment.qualitatively)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(qualitatively=message.text)
        await message.answer("Сотрудники работают по чек листу кофейни?")
        await Comment.next()

    @dp.message_handler(state=Comment.check)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(check=message.text)
        await message.answer("Уголок потребителя содержится в чистоте, без пыли, грязи, паутины, представленная информация корректна и актуальна  Есть КОИП заполненая и в надлежащем состоянии?")
        await Comment.next()

    @dp.message_handler(state=Comment.corner)
    async def process_age(message: types.Message, state: FSMContext):
        await state.update_data(corner=message.text)
        await message.answer("Оценка на Яндексе?")
        await Comment.next()


    @dp.message_handler(state=Comment.yandex)
    async def process_gender(message: types.Message, state: FSMContext):
        async with state.proxy() as data:
            data['yandex'] = message.text

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
                    md.text('25.Оценка на Яндексе:', data['yandex']),
                    sep='\n',
                ),
            )
        await message.answer("Вернулись в главное меню", reply_markup=markup5)
        await state.finish()