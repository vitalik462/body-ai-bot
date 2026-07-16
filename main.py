import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["💪 План тренировок", "🥗 Питание"],
        ["📊 Мой прогресс", "❓ Советы"]
    ]

    await update.message.reply_text(
        "Привет! Я ИИ-помощник по улучшению тела.\n\n"
        "Помогу составить план тренировок, питания и улучшить форму.\n\n"
        "Выбери действие:",
        reply_markup=ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    )


async def message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if "Трениров" in text:
        answer = (
            "💪 Базовый план:\n"
            "• 3 тренировки в неделю\n"
            "• Приседания\n"
            "• Отжимания\n"
            "• Планка\n"
            "• Ходьба 30 минут"
        )

    elif "Питание" in text:
        answer = (
            "🥗 Основы питания:\n"
            "• Больше белка\n"
            "• Овощи каждый день\n"
            "• Достаточно воды\n"
            "• Меньше сладких напитков"
        )

    elif "Прогресс" in text:
        answer = "📊 Напиши свой вес, рост и цель — я помогу оценить прогресс."

    else:
        answer = (
            "❓ Расскажи:\n"
            "1. Твой возраст\n"
            "2. Рост\n"
            "3. Вес\n"
            "4. Цель (масса, похудение, форма)"
        )

    await update.message.reply_text(answer)


def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, message)
    )

    app.run_polling()


if __name__ == "__main__":
    main()
