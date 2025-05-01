from datetime import datetime, timedelta

class Pokemon:
    pokemons = {}

    def __init__(self, username):
        self.username = username
        self.hp = 100
        self.last_feed_time = datetime.now()  # Attribute to track last feeding
        Pokemon.pokemons[username] = self

    def feed(self, feed_interval=20, hp_increase=10):
        current_time = datetime.now()
        delta_time = timedelta(seconds=feed_interval)

        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Health increased! Current health: {self.hp}"
        else:
            next_feed_time = self.last_feed_time + delta_time
            return f"You can feed again at: {next_feed_time.strftime('%H:%M:%S')}"

class Wizard(Pokemon):
    def feed(self, feed_interval=15, hp_increase=10):  # Reduced interval
        return super().feed(feed_interval, hp_increase)

class Fighter(Pokemon):
    def feed(self, feed_interval=20, hp_increase=15):  # Increased HP gain
        return super().feed(feed_interval, hp_increase)
