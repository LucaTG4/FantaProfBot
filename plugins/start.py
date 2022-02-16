from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
prefixes = [",", "+", ".", "/", "!"]

@Client.on_message(filters.command("start", prefixes) & filters.private)
def account(app, msg):
    chat_id = msg.chat.id
    username = msg.from_user.username
    id = msg.from_user.id
    app.send_message(chat_id, f'''👋🏻 Ciao {msg.from_user.mention} 
benvenuto nel FantaProfBot.
''',
                reply_markup=InlineKeyboardMarkup(
                         [
                             [
                                 InlineKeyboardButton("CLASSIFICA", callback_data=f'classifica'),
                                 InlineKeyboardButton("SQUADRE", callback_data=f'squadre')
                             ],
                             [   InlineKeyboardButton("PUNTI", callback_data=f'punti'), 
                             ]
                         ]
                     ),
                     )
    
if data == 'classifica':
  app.edit_message_text(chat_id, message_id, '''i''')
