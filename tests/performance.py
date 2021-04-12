"""
Ensures it can read and write to the file
"""

import guildreader
import unittest
import random
import time

class FakeGuild:
    def __init__(self):
        self.id = random.randint(1, 1000)


class FakeBot:
    def __init__(self):
        self.guilds = []
        for _ in range(7500):
            self.guilds += [FakeGuild()]


class Performance(unittest.TestCase):
    def setUp(self):
        self.bot = FakeBot()
        self.delta = time.time()

    def step1(self):
        guildreader.create_file(self.bot, "test", {"A": 10, "B": [1,2,3,4]}, wipe=True)
        self.create = time.time()

    def step2(self):
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data["A"] == 10
            assert data["B"] == [1,2,3,4]
        self.read = time.time()

    def step3(self):
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            data["A"] = 80
            data["B"] = [1,2,3,4,5,6,8,9,10]
            guildreader.write_file(guild.id, "test", data)
        self.write = time.time()

    def step4(self):
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data["A"] == 80
            assert data["B"] == [1,2,3,4,5,6,8,9,10]
        self.reread = time.time()

    def _steps(self):
        for name in dir(self):  # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()

        curtime = time.time()
        print(f"Total: {curtime-self.delta} Seconds")
        print(f"Create: {curtime - self.create} Seconds")
        print(f"Read: {curtime - self.read} Seconds")
        print(f"Write: {curtime - self.write} Seconds")
        print(f"Reread: {curtime - self.reread} Seconds")


if __name__ == '__main__':
    unittest.main()
