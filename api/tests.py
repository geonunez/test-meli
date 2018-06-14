# -*- coding: utf-8 -*-

from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

class MutantTestCase(TestCase):


    def test_invalid_parameters(self):
        adns = [
            # Not has then minimun len
            [
                'AAA',
                'CCC',
                'TTT'
            ],
            # Not is a NxN
            [
                'AAAA',
                'CCCC',
                'TTTT'
            ],
            [
                'AAA',
                'CCC',
                'TTT',
                'GGG'
            ],
            [
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
                'ACACACCACACACACACACACACAC',
                'TGTGATGAAATGGGGAAAAAAATGG',
            ],
            # Some column breaks the matrix len
            [
                'AAAA',
                'TTT',
                'GGGG',
                'CCCC'
            ]
        ]

        for adn in adns:
            client = APIClient()
            response = client.post('/api/v1/mutant', { 'adn': adn }, format='json')
            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

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
            client = APIClient()
            response = client.post('/api/v1/mutant', { 'adn': adn }, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)


