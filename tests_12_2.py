import unittest
from runner import Runner, Tournament


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.usein = Runner('Усейн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nik = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(elem)

    def test_fist_tur(self):
        tur = Tournament(90, self.usein, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')

    def test_second_tur(self):
        tur = Tournament(90, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2], 'Ник')

    def test_third_tur(self):
        tur = Tournament(90, self.usein, self.andrey, self.nik)
        result = {k: str(v) for k, v in tur.start().items()}

        TournamentTest.all_results.append(result)
        self.assertTrue(result[3], 'Ник')