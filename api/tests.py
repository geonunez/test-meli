from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

class MutantTestCase(TestCase):

    client = APIClient()

    def test_mutant(self):
        adns = [
            # two or more in horizontal
            [
                'AAAA',
                'CCGC',
                'TTTT',
                'AGAG'
            ],
            [
                'ACGA',
                'TTTT',
                'CCCC',
                'AAAA'
            ],
            [
                'TTTT',
                'GGGG',
                'AAAA',
                'CCCC'
            ],
            [
                'TATTCA',
                'TTAAAA',
                'GGGGTA',
                'TCAGCA',
                'CTAGAG',
                'TCCCAG'
            ],
            # two or more in vertical
            [
                'AATA',
                'ACTC',
                'ATTT',
                'AGTG'
            ],
            [
                'TGGT',
                'TGGT',
                'AGGA',
                'CGGC'
            ],
            [
                'ACAA',
                'ACAA',
                'AGAA',
                'ATAA'
            ],
            # two or more in diagonal
            [
                'CCGTTG',
                'CAGGAG',
                'TGACGT',
                'GGGACG',
                'TTTGAT',
                'TGAAGC'
            ],
        ]

        for adn in adns:
            response = self.client.post('/api/v1/mutant', {'adn': adn}, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


