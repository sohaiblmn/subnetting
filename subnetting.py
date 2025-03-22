from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext
import ipaddress
import os

TOKEN = os.getenv("7861383816:AAFBgC4etNqLHs91f26z5s24zUC6ejGaxgg")  # اجلب التوكن من المتغيرات البيئية

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("Hello! Send an IP with CIDR like: /subnet 192.168.1.0/24")

async def subnet(update: Update, context: CallbackContext):
    if len(context.args) != 1:
        await update.message.reply_text("Usage: /subnet 192.168.1.0/24")
        return

    try:
        network = ipaddress.ip_network(context.args[0], strict=False)
        response = (
            f"📡 Network Info:\n"
            f"🔹 Network Address: {network.network_address}\n"
            f"🔹 Broadcast Address: {network.broadcast_address}\n"
            f"🔹 Number of Addresses: {network.num_addresses}\n"
            f"🔹 First IP: {list(network.hosts())[0]}\n"
            f"🔹 Last IP: {list(network.hosts())[-1]}\n"
            f"🔹 Subnet Mask: {network.netmask}\n"
        )
        await update.message.reply_text(response)
    except ValueError:
        await update.message.reply_text("⚠️ Invalid IP. Use format: 192.168.1.0/24")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("subnet", subnet))

    print("✅ Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
