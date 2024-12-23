from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN = "_______________________"

movie_recommendations = {
        "Боевик": [
        {"name": "Безумный Макс: Дорога ярости", "link": "https://www.kinopoisk.ru/film/453406/"},
        {"name": "Джон Уик", "link": "https://www.kinopoisk.ru/film/762738/"},
        {"name": "Тёмный рыцарь", "link": "https://www.kinopoisk.ru/film/111543/"},
        {"name": "Гладиатор", "link": "https://www.kinopoisk.ru/film/474/"},
        {"name": "Крепкий орешек", "link": "https://www.kinopoisk.ru/film/471/"},
        {"name": "Мстители", "link": "https://www.kinopoisk.ru/film/263531/"},
        {"name": "Мстители: Война бесконечности", "link": "https://www.kinopoisk.ru/film/843649/"},
        {"name": "Чёрная пантерa", "link": "https://www.kinopoisk.ru/film/623250/"},
        {"name": "Бэтмен: Начало", "link": "https://www.kinopoisk.ru/film/47237/"},
        {"name": "Рэмбо: Первая кровь", "link": "https://www.kinopoisk.ru/film/4087/"},
    ],
        "Комедия": [
        {"name": "Мальчишник в Вегасе", "link": "https://rutube.ru/video/5d5e80b016776124cac07a95e97804ac/"},
        {"name": "SuperПерцы", "link": "https://www.kinopoisk.ru/film/261363/"},
        {"name": "Монти Пайтон и Священный Грааль", "link": "https://rutube.ru/video/2ffcaf115cf786ebbb99ee44d83523f9/"},
        {"name": "Сводные братья", "link": "https://rutube.ru/video/688a8af2468f7eecc8ee9da05c9809f0/"},
        {"name": "Большой Лебовски", "link": "https://www.kinopoisk.ru/film/555/"},
        {"name": "День сурка", "link": "https://www.kinopoisk.ru/film/527/"},
        {"name": "Семейка Аддамс", "link": "https://www.kinopoisk.ru/film/5293/"},
        {"name": "Гарольд и Мод", "link": "https://www.kinopoisk.ru/film/20049/"},
        {"name": "Охотники за привидениями", "link": "https://www.kinopoisk.ru/film/2467/"},
        {"name": "Иван Васильевич меняет профессию", "link": "https://www.kinopoisk.ru/film/42664/"}
    ],
        "Драма": [
        {"name": "Побег из Шоушенка", "link": "https://rutube.ru/video/a40f9d0d584876667786155a9e9fd564/"},
        {"name": "1+1", "link": "https://www.kinopoisk.ru/film/535341/"},
        {"name": "Крёстный отец", "link": "https://rutube.ru/video/6c9f685c1dea6e3e306849e29152546d/"},
        {"name": "Список Шиндлера", "link": "https://rutube.ru/video/deca8ef2a127c79464a8404f8d2aa7b2/"},
        {"name": "Игры разума", "link": "https://www.kinopoisk.ru/film/530/"},
        {"name": "Зеленая миля", "link": "https://www.kinopoisk.ru/film/435/"},
        {"name": "Форрест Гамп", "link": "https://www.kinopoisk.ru/film/448/"},
        {"name": "Бойцовский клуб", "link": "https://www.kinopoisk.ru/film/361/"},
        {"name": "Далласский клуб покупателей", "link": "https://www.kinopoisk.ru/film/260162/"},
        {"name": "Брат", "link": "https://www.kinopoisk.ru/film/41519/"}
    ],
        "Ужасы": [
        {"name": "Изгоняющий дьявола", "link": "https://www.kinopoisk.ru/film/491/"},
        {"name": "Заклятие", "link": "https://www.kinopoisk.ru/film/468994/"},
        {"name": "Оно", "link": "https://www.kinopoisk.ru/film/453397/"},
        {"name": "Кошмар на улице Вязов", "link": "https://rutube.ru/video/07fb5afcc7dfb33369737f7be985a302/"},
        {"name": "Сияние", "link": "https://rutube.ru/video/6f019640e95283617cc0d1eae0d8bf4b/"},
        {"name": "Чужой", "link": "https://www.kinopoisk.ru/film/386/"},
        {"name": "Звонок", "link": "https://www.kinopoisk.ru/film/804/"},
        {"name": "Паранормальное явление", "link": "https://www.kinopoisk.ru/film/404366/"},
        {"name": "Техасская резня бензопилой", "link": "https://www.kinopoisk.ru/film/16015/"},
        {"name": "Семь", "link": "https://www.kinopoisk.ru/film/377/"}
    ],
        "Фантастика": [
        {"name": "Начало", "link": "https://www.kinopoisk.ru/film/447301/"},

        {"name": "Интерстеллар", "link": "https://www.kinopoisk.ru/film/258687/"},
        {"name": "Матрица", "link": "https://rutube.ru/video/06f4c1dd1b319392aedc768867b4980f/"},
        {"name": "Бегущий по лезвию 2049", "link": "https://rutube.ru/video/fbd9299eca041a8260dcb83394271af0/"},
        {"name": "Звёздные войны: Новая надежда", "link": "https://www.kinopoisk.ru/film/333/"},
        {"name": "Грань будущего", "link": "https://www.kinopoisk.ru/film/505851/"},
        {"name": "Время", "link": "https://www.kinopoisk.ru/film/517988/"},
        {"name": "Обливион", "link": "https://www.kinopoisk.ru/film/470185/"},
        {"name": "Космическая одиссея 2001", "link": "https://www.kinopoisk.ru/film/8880/"},
        {"name": "Трасса 60", "link": "https://www.kinopoisk.ru/film/3563/"}
    ]
}
def create_genre_keyboard():
    keyboard = [
        [InlineKeyboardButton("Боевик", callback_data="Боевик")],
        [InlineKeyboardButton("Комедия", callback_data="Комедия")],
        [InlineKeyboardButton("Драма", callback_data="Драма")],
        [InlineKeyboardButton("Ужасы", callback_data="Ужасы")],
        [InlineKeyboardButton("Фантастика", callback_data="Фантастика")],
        [InlineKeyboardButton("Поиск по названию", callback_data="search")],
        [InlineKeyboardButton("Тест: Какой ты киноперсонаж?", callback_data="test_character")]
    ]
    return InlineKeyboardMarkup(keyboard)

async def show_main_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = create_genre_keyboard()
    if update.callback_query:
        await update.callback_query.message.reply_text("Выбери жанр или опцию:", reply_markup=reply_markup)
    elif update.message:
        await update.message.reply_text("Выбери жанр или опцию:", reply_markup=reply_markup)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['expecting_name'] = True
    await update.message.reply_text("Здравствуй, дорогой любитель кино! Как тебя зовут?")

async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('expecting_name'):
        user_name = update.message.text
        context.user_data['user_name'] = user_name
        context.user_data['expecting_name'] = False

        reply_markup = create_genre_keyboard()
        await update.message.reply_text(
            f"Приятно познакомиться, {user_name}! Нажми на кнопку с жанром, чтобы получить рекомендации:",
            reply_markup=reply_markup
        )

async def handle_genre_selection(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    genre = query.data

    if genre in movie_recommendations:
        movies = movie_recommendations[genre]
        response = f"Вот рекомендации для жанра {genre}:\n"
        for movie in movies:
            response += f"- [{movie['name']}]({movie['link']})\n"
        await query.message.reply_text(response, parse_mode="Markdown")
    else:
        await query.message.reply_text("Жанр не найден. Попробуйте снова.")

    await show_main_menu(update, context)

async def handle_search(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    context.user_data['expecting_search'] = True
    await query.message.reply_text("Введите название фильма для поиска:")

async def handle_search_input(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('expecting_search'):
        movie_name = update.message.text
        context.user_data['expecting_search'] = False
        found_movies = []

        # Ищем фильм по названию
        for genre, movies in movie_recommendations.items():
            for movie in movies:
                if movie_name.lower() in movie['name'].lower():
                    found_movies.append(movie)


        if found_movies:
            response = "Вот что я нашел по запросу:\n"
            for movie in found_movies:
                response += f"- [{movie['name']}]({movie['link']})\n"
            await update.message.reply_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text("Не найдено фильмов с таким названием.")

        await show_main_menu(update, context)

#обработчик для имени пользователя
async def handle_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.user_data.get('expecting_name'):
        user_name = update.message.text
        context.user_data['user_name'] = user_name
        context.user_data['expecting_name'] = False

        reply_markup = create_genre_keyboard()
        await update.message.reply_text(
            f"Приятно познакомиться, {user_name}! Нажми на кнопку с жанром, чтобы получить рекомендации:",
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(
    filters.TEXT & ~filters.COMMAND,
    lambda update, context: (
        handle_name(update, context) if context.user_data.get('expecting_name') else handle_search_input(update, context)
    )
))
app.add_handler(CallbackQueryHandler(handle_genre_selection, pattern="^(Боевик|Комедия|Драма|Ужасы|Фантастика)$"))
app.add_handler(CallbackQueryHandler(handle_search, pattern="search"))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_search_input))

async def handle_test_character(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user_name = context.user_data.get('user_name', 'друг')
    await query.answer()

    #тест первый вход
    if 'test_stage' not in context.user_data or context.user_data['test_stage'] == 0:
        context.user_data['test_stage'] = 0
        context.user_data['test_answers'] = []

    test_questions = [
        {
            "question": "Вы....",
            "options": [
                {
        "text": "Оптимист",
        "data": ["Тони Старк", "Джек Воробей"]
    },
    {
        "text": "Пессимист",
        "data": ["Джокер", "Джон Уик"]
    },
    {
        "text": "Реалист",
        "data": ["Супермен", "Доктор Стрендж"]
    }
                
            ]
        },
        {
            "question": "Какой твой главный приоритет в жизни?",
            "options": [
                {"text": "Свобода и независимость", "data": "Джон Уик"},
                {"text": "Защищать тех, кто мне дорог", "data": "Супермен"},
                {"text": "Достигать успеха любой ценой", "data": "Тони Старк"},
                {"text": "Стремление к знаниям и открытиям", "data": "Доктор Стрендж"},
                {"text": "Мечтаю о приключениях и поисках новых горизонтов", "data": "Капитан Джек Воробей"},
                {"text": "Создавать хаос вокруг себя", "data": "Джокер"}
            ]
        },
        {
            "question": "Как ты предпочитаешь решать проблемы?",
            "options": [
                {"text": "Быстро действую, не раздумывая", "data": "Джон Уик"},
                {"text": "Сначала анализирую, а потом принимаю решение", "data": "Супермен"},
                {"text": "Действуем, детали обговорим потом", "data": "Тони Старк"},
                {"text": "Я исследую все возможные варианты, чтобы найти лучшее решение", "data": "Доктор Стрендж"},
                {"text": "Использую хитрость и смекалку, чтобы выйти из ситуации", "data": "Капитан Джек Воробей"},
                {"text": "Ищу способ нарушить все правила и создать свой порядок", "data": "Джокер"}
            ]
        },
        {
            "question": "Какой твой любимый способ отдыха?",
            "options": [
                {"text": "Одиночество и свобода, чтобы восстановить силы", "data": "Джон Уик"},
                {"text": "Провести время с близкими, делая что-то важное вместе", "data": "Супермен"},
                {"text": "Преодолевать трудности и достигать целей", "data": "Тони Старк"},
                {"text": "Чтение книг или изучение нового", "data": "Доктор Стрендж"},
                {"text": "Путешествия и приключения", "data": "Капитан Джек Воробей"},
                {"text": "Организация веселья и нестандартных ситуаций", "data": "Джокер"}
            ]
        }
    ]

    stage = context.user_data['test_stage']
    if stage < len(test_questions):
        question = test_questions[stage]
        keyboard = [
            [InlineKeyboardButton(option["text"], callback_data=f"test_{option['data']}")]
            for option in question["options"]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.message.reply_text(question["question"], reply_markup=reply_markup)
        context.user_data['test_stage'] += 1
    else:
        result = analyze_test_result(context.user_data['test_answers'])
        await query.message.reply_text(f"{user_name}, ты {result}!")
        context.user_data['test_stage'] = 0
        context.user_data['test_answers'] = []

        # Возврат в главное меню
        await show_main_menu(update, context)


def analyze_test_result(answers):
    if "Джон Уик" in answers:
        return "Джон Уик! Ты ценишь свою свободу и готов(а) на всё ради неё. Ты не боишься действовать решительно и без колебаний"
    elif "Супермен" in answers:
        return "Супермен! Ты всегда готов(а) защищать тех, кого любишь. Ты — настоящий защитник, готовый принять на себя ответственность"
    elif "Тони Старк" in answers:
        return "Тони Старк! Человек, который всегда стремится быть первым. Ты не боишься рисковать и идти на жертвы ради достижения своей цели. Твои амбиции и решимость вдохновляют окружающих"
    elif "Доктор Стрендж" in answers:
        return "Доктор Стрендж! Ты всегда ищешь ответы на глубокие вопросы и стремишься к познанию. Тебя не пугают трудности"
    elif "Капитан Джек Воробей" in answers:
        return "Капитан Джек Воробей! Ты ценишь свою свободу и независимость. Тебе нравится жизнь, полная приключений, неожиданных поворотов и рисков"
    elif "Джокер" in answers:
        return "Джокер! Ты живешь ради хаоса и разрушения. Ты не боишься манипулировать людьми, чтобы достичь своей цели"
    else:
        return "Вернемся к меню"

async def handle_test_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    answer = query.data.replace("test_", "")
    context.user_data['test_answers'].append(answer)
    await handle_test_character(update, context)

app.add_handler(CallbackQueryHandler(handle_test_character, pattern="test_character"))
app.add_handler(CallbackQueryHandler(handle_test_answer, pattern="test_.*"))


app.run_polling()
