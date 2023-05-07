from pyrogram import Client, filters

api_id = 2951422
api_hash = "a02754a31502b9c75727a0c555501590"
bot_token = "6120020304:AAHD15wBZQqM1x5780jHe5g5SV6GSOyfong"

app = Client("Moonsunverse_bot", api_id, api_hash, bot_token)

print("Bot yaratildi!")



# # !pip install pyrogram
# from pyrogram import Client, filters


# admin IDlarini saqlash
admin_ids = {936911586, 5876839412}

@app.on_message(filters.command("start"))
def start_command(client, message):
    # Foydalanuvchining ma'lumotlarini saqlash
    user_id = message.chat.id
    first_name = message.chat.first_name
    last_name = message.chat.last_name
    username = message.chat.username
    
    # Xabar yuborish
    message.reply_text("Salom! Bu anonim chat botiga hush kelibsiz.")

@app.on_message(~filters.command("start"))
def handle_message(client, message):
    # Foydalanuvchining xabarini topish
    user_id = message.chat.id
    
    # Xabar yuborish
    for admin_id in admin_ids:
        client.send_message(chat_id=admin_id, text=f"Anonim xabar:\n{message.text}")


# Kanalga xabar yuborish
app.send_message(chat_id="Moonsunverse", text="Salom, bu botdan xabar!")

@app.catch_all()
def catch_all_handler(client, message):
    # Blok ochish
    print("This is a catch-all handler.")
    client.send_message(
        chat_id=message.chat.id,
        text=f"Sorry, I don't understand this command: {message.text}"
    )
    # Blok yopish
app.run()