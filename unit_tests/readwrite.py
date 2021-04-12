"""
Ensures it can read and write to the file
"""

import guildreader
import unittest
import random


class FakeGuild:
    def __init__(self):
        self.id = random.randint(1, 1000)


class FakeBot:
    def __init__(self):
        self.guilds = []
        for _ in range(30):
            self.guilds += [FakeGuild()]


class ReadWrite(unittest.TestCase):
    def setUp(self):
        self.bot = FakeBot()

    def step1(self):
        guildreader.create_file(self.bot, "test", "Yes", wipe=True)

    def step2(self):
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data == "Yes"

    def step3(self):
        for guild in self.bot.guilds:
            guildreader.write_file(guild.id, "test", "rewrite")

    def step4(self):
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data == "rewrite"

    def _steps(self):
        for name in dir(self):  # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()


if __name__ == '__main__':
    unittest.main()
