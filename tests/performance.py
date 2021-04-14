"""
Ensures it can read and write to the file
"""

import guildreader
import unittest
import random
import time


class FakeGuild:
    def __init__(self):
        self.id = random.randint(1, 999999999)


class FakeBot:
    def __init__(self):
        self.guilds = []
        for _ in range(1000):
            self.guilds += [FakeGuild()]


# noinspection PyAttributeOutsideInit
class Performance(unittest.TestCase):
    def setUp(self):
        self.bot = FakeBot()
        self.delta = time.time()

    def step1(self):
        delta = time.time()
        guildreader.create_file(self.bot, "test", {"A": 10, "B": [1, 2, 3, 4]}, wipe=True)
        print(f'Creation Time: {time.time()-delta} seconds...')

    def step2(self):
        delta = time.time()
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data["A"] == 10
            assert data["B"] == [1, 2, 3, 4]
        print(f'Full Read Time: {time.time()-delta} seconds...')

    def step3(self):
        delta = time.time()
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            data["A"] = 80
            data["B"] = [1, 2, 3, 4, 5, 6, 8, 9, 10]
            guildreader.write_file(guild.id, "test", data)
        print(f'Full Write Time: {time.time()-delta} seconds...')

    def step4(self):
        delta = time.time()
        for guild in self.bot.guilds:
            data = guildreader.read_file(guild.id, "test")
            assert data["A"] == 80
            assert data["B"] == [1, 2, 3, 4, 5, 6, 8, 9, 10]
        print(f'Full Reread Time: {time.time()-delta} seconds...')

    def step5(self):
        delta = time.time()
        guildreader.create_file(self.bot, "test", {"A": 10, "B": [1, 2, 3, 4]}, wipe=True)
        print(f'Recreation Time: {time.time()-delta} seconds...')

    def step6(self):
        delta = time.time()
        data = guildreader.read_file(self.bot.guilds[0].id, "test")
        assert data["A"] == 10
        assert data["B"] == [1, 2, 3, 4]
        print(f'Single Read Time: {time.time() - delta} seconds...')

    def step7(self):
        delta = time.time()
        data = guildreader.read_file(self.bot.guilds[0].id, "test")
        data["A"] = 80
        data["B"] = [1, 2, 3, 4, 5, 6, 8, 9, 10]
        guildreader.write_file(self.bot.guilds[0], "test", data)
        print(f'Single Write Time: {time.time() - delta} seconds...')

    def step8(self):
        delta = time.time()
        data = guildreader.read_file(self.bot.guilds[0].id, "test")
        assert data["A"] == 80
        assert data["B"] == [1, 2, 3, 4, 5, 6, 8, 9, 10]
        print(f'Single Reread Time: {time.time() - delta} seconds...')

    def _steps(self):
        for name in dir(self):  # dir() result is implicitly sorted
            if name.startswith("step"):
                yield name, getattr(self, name)

    def test_steps(self):
        for name, step in self._steps():
            step()


if __name__ == '__main__':
    unittest.main()
