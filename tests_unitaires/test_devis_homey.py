import unittest
from devis_homey import devis_par_nuit


class TestSolutionLesson2(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(devis_par_nuit(100.0, week_end=True, long_sejour=True), 105.0)


# TODO : Continuer depuis la leçon 2 et ajouter les tests manquants
# 1. Ajouter le test week_end=False et long_sejour=False
# 2. Ajouter le test week_end=True et long_sejour=False


if __name__ == "__main__":
    unittest.main()