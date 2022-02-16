from pyrogram import Client
from pyrogram import filters
from pyrogram import idle
import time 
prefixes = [",", "+", ".", "/", "!"]


app = Client(
    "my_bot",
    bot_token="5235094268:AAH0dnnxuMU8T9J2La3_C3GsCP0dWD2_Vzg",
    api_id=1561405,
    api_hash="a38135e34dbecb5032d22d5739a6b967",
    plugins=dict(root="plugins"),
)

app.run()
