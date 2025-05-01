@bot.message_handler(commands=['feed'])
def feed_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons.keys():
        result = Pokemon.pokemons[username].feed()
        bot.send_message(message.chat.id, result)
    else:
        bot.send_message(message.chat.id, "You need a Pokémon before feeding!")
