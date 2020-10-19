import os
import text

from pyrogram import Client, filters

from chars import chars


api_id = os.environ.get('api_id') 
api_hash = os.environ.get('api_hash') 
print(os.environ)
app = Client("matrix_bot", api_id, api_hash)

color = (10, 10, 10)

@app.on_message(filters.private & filters.incoming)
def new_message(client, message):
    if all(char in chars.keys() for char in message.text):
        text.main(message.text, color)

app.run()
