# Контролер телевізора
# Створіть простий прототип ТВ-контролера на Python. Він використовуватиме такі команди:
# first_channel() - вмикає перший канал зі списку.
# last_channel() - вмикає останній канал зі списку.
# turn_channel(N) - вмикає N канал. Зверніть увагу, що номери каналів починаються з 1, а не з 0.
# next_channel() - вмикає наступний канал. Якщо поточний канал останній, вмикається перший канал.
# previous_channel() - вмикає попередній канал. Якщо поточний канал є першим, вмикається останній канал.
# current_channel() - повертає назву поточного каналу.
# is_exist(N/'name') - отримує 1 аргумент - число N або рядок "name" і повертає "Yes",
# якщо канал N або "name" існує в списку, або "No" - в іншому випадку .
# Канал за замовчуванням увімкнено перед усіма командами – №1.
# Ваше завдання — створити клас і методи TVController, описані вище.
# CHANNELS = ["BBC", "Discovery", "TV1000"]
#  class TVController:
#
# pass
#
#  controller = TVController(CHANNELS)
#
# controller.first_channel() == "BBC"
#
# controller.last_channel() == "TV1000"
#
# controller.turn_channel(1) == "BBC"
#
# controller.next_channel() == "Discovery"
#
# controller.previous_channel() == "BBC"
#
# controller.current_channel() == "BBC"
#
# controller.is_exist(4) == "No"
#
# controller.is_exist("BBC") == "Yes"
CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:
    def __init__(self, channels: list):
        self.channels = channels
        self.active_channel = channels[0]

    def first_channel(self) -> str:
        """Вмикає перший канал зі списку"""
        print(self.channels[0])

    def last_channel(self) -> str:
        """Вмикає останній канал зі списку"""
        print(self.channels[-1])

    def turn_channel(self, what_turn: int) -> str:
        """Вмикає N канал"""
        self.active_channel = self.channels[what_turn - 1]
        print(self.active_channel)

    def next_channel(self) -> str:
        """Вмикає наступний канал. Якщо поточний канал останній, вмикається перший канал"""
        if self.active_channel != self.channels[-1]:
            self.active_channel = self.channels[0]
            print(self.active_channel)
        self.active_channel = self.channels[self.channels.index(self.active_channel) + 1]
        print(self.active_channel)

    def previous_channel(self):
        pass

    def current_channel(self):
        pass

    def is_exist(self, name):
        pass

controller = TVController(CHANNELS)
controller.first_channel()
controller.last_channel()
controller.turn_channel(1)
controller.next_channel()