from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

TELEGRAM_TOKEN = "______"

movie_recommendations = {
    "Боевик": [
        {"name": "Безумный Макс: Дорога ярости", "link": "https://www.kinopoisk.ru/film/453406/"},
        {"name": "Джон Уик", "link": "https://www.kinopoisk.ru/film/762738/"},
        {"name": "Тёмный рыцарь", "link": "https://www.kinopoisk.ru/film/111543/"},
        {"name": "Гладиатор", "link": "https://www.kinopoisk.ru/film/474/"},
        {"name": "Крепкий орешек", "link": "https://www.kinopoisk.ru/film/471/"},
    ],
    "Комедия": [
        {"name": "Мальчишник в Вегасе", "link": "https://rutube.ru/video/5d5e80b016776124cac07a95e97804ac/"},
        {"name": "SuperПерцы", "link": "https://www.kinopoisk.ru/film/261363/"},
        {"name": "Монти Пайтон и Священный Грааль", "link": "https://rutube.ru/video/2ffcaf115cf786ebbb99ee44d83523f9/"},
        {"name": "Сводные братья", "link": "https://rutube.ru/video/688a8af2468f7eecc8ee9da05c9809f0/"},
        {"name": "Большой Лебовски", "link": "https://www.kinopoisk.ru/film/555/"},
    ],
    "Драма": [
        {"name": "Побег из Шоушенка", "link": "https://rutube.ru/video/a40f9d0d584876667786155a9e9fd564/"},
        {"name": "1+1", "link": "https://www.kinopoisk.ru/film/535341/"},
        {"name": "Крёстный отец", "link": "https://rutube.ru/video/6c9f685c1dea6e3e306849e29152546d/"},
        {"name": "Список Шиндлера", "link": "https://rutube.ru/video/deca8ef2a127c79464a8404f8d2aa7b2/"},
        {"name": "Игры разума", "link": "https://www.kinopoisk.ru/film/530/"},
    ],
    "Ужасы": [
        {"name": "Изгоняющий дьявола", "link": "https://www.kinopoisk.ru/film/491/"},
        {"name": "Заклятие", "link": "https://www.kinopoisk.ru/film/468994/"},
        {"name": "Оно", "link": "https://www.kinopoisk.ru/film/453397/"},
        {"name": "Кошмар на улице Вязов", "link": "https://rutube.ru/video/07fb5afcc7dfb33369737f7be985a302/"},
        {"name": "Сияние", "link": "https://rutube.ru/video/6f019640e95283617cc0d1eae0d8bf4b/"},
    ],
    "Фантастика": [
        {"name": "Начало", "link": "https://www.kinopoisk.ru/film/447301/"},
        {"name": "Интерстеллар", "link": "https://www.kinopoisk.ru/film/258687/"},
        {"name": "Матрица", "link": "https://rutube.ru/video/06f4c1dd1b319392aedc768867b4980f/"},
        {"name": "Бегущий по лезвию 2049", "link": "https://rutube.ru/video/fbd9299eca041a8260dcb83394271af0/"},
        {"name": "Звёздные войны: Новая надежда", "link": "https://www.kinopoisk.ru/film/333/"},
    ]
}

def create_genre_keyboard():
    keyboard = [
        [InlineKeyboardButton("Боевик", callback_data="Боевик")],
        [InlineKeyboardButton("Комедия", callback_data="Комедия")],
        [InlineKeyboardButton("Драма", callback_data="Драма")],
        [InlineKeyboardButton("Ужасы", callback_data="Ужасы")],
        [InlineKeyboardButton("Фантастика", callback_data="Фантастика")],
    ]
    return InlineKeyboardMarkup(keyboard)

async def start(update: Update, context):
    reply_markup = create_genre_keyboard()
    await update.message.reply_text(
        "Привет! Я помогу тебе выбрать фильм. Нажми на кнопку с жанром, чтобы получить рекомендации:",
        reply_markup=reply_markup
    )

async def recommend(update: Update, context):
    query = update.callback_query
    genre = query.data
    await query.answer()

    if genre in movie_recommendations:
        movies = movie_recommendations[genre]
        recommendation_text = f"Вот фильмы в жанре '{genre}':\n"
        for movie in movies:
            recommendation_text += f"- [{movie['name']}]({movie['link']})\n"
        await query.edit_message_text(
            text=recommendation_text, 
            parse_mode="Markdown"
        )

    reply_markup = create_genre_keyboard()
    await query.message.reply_text(
        "Выбери ещё жанр, чтобы получить рекомендации:",
        reply_markup=reply_markup
    )

def main():

    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(recommend))

    application.run_polling()

if __name__ == "__main__":
    main()
