from django.test import TestCase

from .services import MutantService

class MutantTestCase(TestCase):

    mutantService = MutantService()

    def test_mutant(self):
        adns = [
            # two in horizontal
            ['AAAAGA', 'CCCCGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG'],
            ['ATGCGA', 'CAGTGC', 'TTATGT', 'AGAAGG', 'CCCCTA', 'TCACTG'],
        ]

        for adn in adns:
            response = self.mutantService.is_mutant(adn)
            self.assertEqual(response, True)


