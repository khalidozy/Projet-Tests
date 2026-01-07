import unittest
from devis_homey import devis_par_nuit


class TestSolutionLesson3(unittest.TestCase):
    def test_basic_case(self):
        # Test from lesson 2: week_end=True et long_sejour=True
        # Ce test couvre toutes les instructions mais seulement 2 des 4 branches
        self.assertEqual(devis_par_nuit(100.0, week_end=True, long_sejour=True), 105.0)

    def test_week_end_faux_long_faux(self):
        # Test ajouté pour couvrir: week_end=False, long_sejour=False
        self.assertEqual(devis_par_nuit(100.0, week_end=False, long_sejour=False), 100.0)

    def test_week_end_vrai_long_faux(self):
        # Test ajouté pour couvrir: week_end=True, long_sejour=False
        self.assertEqual(devis_par_nuit(100.0, week_end=True, long_sejour=False), 115.0)


if __name__ == '__main__':
    unittest.main()