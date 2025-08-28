from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7228581207:AAFop_0X4zKKZgn6GYU5geglAponPq6dZAc"  # Reemplaza con el token de tu bot
ADMIN_CHAT_ID = 6530133583  # Reemplaza con tu chat ID (entero, sin comillas)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "¡Hola! Soy tu bot de pedidos de animes para CARDINAL ISEKAI. Usa /pedido <nombre del anime> para hacer un pedido."
    )

async def pedido(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        anime = " ".join(context.args)
        user = update.effective_user
        pedido_msg = (
            f"Pedido recibido de @{user.username or user.first_name}:\nAnime: {anime}"
        )
        await update.message.reply_text(
            f"Pedido recibido para el anime: {anime}.\n¡¡Muchas gracias por su pedido, tan pronto se descargue se estara subiendo el anime al canal!"
        )
        # Enviar mensaje privado al admin
        await context.bot.send_message(
            chat_id=ADMIN_CHAT_ID,
            text=pedido_msg
        )
    else:
        await update.message.reply_text("Por favor, indica el nombre del anime. Ejemplo: /pedido Naruto")

async def ayuda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Iniciar bot\n"
        "/pedido <nombre> - Pedir un anime\n"
        "/ayuda - Mostrar ayuda"
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("pedido", pedido))
    app.add_handler(CommandHandler("ayuda", ayuda))

    print("Bot corriendo...")
    app.run_polling()