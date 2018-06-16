# -*- coding: utf-8 -*-

import time

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from .models import Human

class IndexTextCase(TestCase):
    client = APIClient()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertJSONEqual(response.content, { \
            'title': 'Geonunez Test Meli' \
        })

class HumanTestCase(TestCase):
    client = APIClient()

    def test_invalid_parameters(self):
        dnas = [
            # Not has then minimun len
            ['AAA', 'CCC', 'TTT'],
            # Not is a NxN
            ['AAAA', 'CCCC', 'TTTT'],
            ['AAA', 'CCC', 'TTT', 'GGG'],
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
            ['AAAA', 'TTT', 'GGGG', 'CCCC']
        ]

        for dna in dnas:
            s_dna = ''.join(dna)
            response = self.client.post('/api/v1/mutant', { 'dna': dna }, format='json')
            how_many = Human.objects.filter(dna=s_dna).count()

            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            self.assertEqual(how_many, 0)

    def test_mutant(self):
        dnas = [
            # two or more in →
            ['AAAA', 'CCGC', 'TTTT', 'AGAG'],
            ['ACGA', 'TTTT', 'CCCC', 'AAAA'],
            ['TTTT', 'GGGG', 'AAAA', 'CCCC'],
            ['TATTCA', 'TTAAAA', 'GGGGTA', 'TCAGCA', 'CTAGAG', 'TCCCAG'],
            # two or more in ↓
            ['AATA', 'ACTC', 'ATTT', 'AGTG'],
            ['TGGT', 'TGGT', 'AGGA', 'CGGC'],
            ['ACAA', 'ACAA', 'AGAA', 'ATAA'],
            # two or more in ↘
            ['CCGTTG','CAGGAG','TGACGT','GGGACG','TTTGAT','TGAAGC'],
            # two or more in ↗
            ['CCGTTG', 'CAGTAG', 'TGTCGT', 'GTGGCG', 'TTGGTT', 'TGAAGC'],
            # two or more in →↗↘↓
            ['CCGTTG', 'CAGTAG', 'TGGCGT', 'GGGGCG', 'TTGGTT', 'TGGAGC'],
            # Repeated ones
            ['AAAA', 'CCGC', 'TTTT', 'AGAG'],
            ['AATA', 'ACTC', 'ATTT', 'AGTG'],
            ['CCGTTG','CAGGAG','TGACGT','GGGACG','TTTGAT','TGAAGC'],
            ['CCGTTG', 'CAGTAG', 'TGTCGT', 'GTGGCG', 'TTGGTT', 'TGAAGC'],
            ['CCGTTG', 'CAGTAG', 'TGGCGT', 'GGGGCG', 'TTGGTT', 'TGGAGC'],
        ]

        for dna in dnas:
            s_dna = ''.join(dna)
            response = self.client.post('/api/v1/mutant', { 'dna': dna }, format='json')
            how_many = Human.objects.filter(dna=s_dna).count()

            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(how_many, 1)

    def test_humans(self):
        dnas = [
            # Zero appears
            ['ATAA', 'CCGC', 'TATT', 'AGAG'],
            ['ACGA', 'TCTT', 'CTCC', 'AAAA'],
            ['TATTCA', 'TTATAA', 'GTGGTA', 'TCAGCA', 'CTAGAG', 'TCCCAG'],
            # One appear
            ['AAAA', 'CCGC', 'TATT', 'AGAG'], # →
            ['ACGA', 'TCTT', 'TCCC', 'ACAA'], # ↓
            ['ACGA', 'TATT', 'TCAC', 'ACAA'], # ↘
            ['ACGA', 'TCAT', 'TACC', 'ACAA'], # ↗
            # Repeated ones
            ['ATAA', 'CCGC', 'TATT', 'AGAG'],
            ['AAAA', 'CCGC', 'TATT', 'AGAG'], # →
            ['ACGA', 'TCTT', 'TCCC', 'ACAA'], # ↓
            ['ACGA', 'TATT', 'TCAC', 'ACAA'], # ↘
            ['ACGA', 'TCAT', 'TACC', 'ACAA'], # ↗
        ]

        for dna in dnas:
            s_dna = ''.join(dna)
            response = self.client.post('/api/v1/mutant', { 'dna': dna }, format='json')
            how_many = Human.objects.filter(dna=s_dna).count()

            self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
            self.assertEqual(how_many, 1)

    def test_stats(self):
        # Check with an empty db
        data = self.client.get('/api/v1/stats').data

        self.assertEqual(data['count_mutant_dna'], 0)
        self.assertEqual(data['count_human_dna'], 0)
        self.assertEqual(data['ratio'], 0)

        # Populate the db
        dnas = [
            # Humans
            ['ATAA', 'CCGC', 'TATT', 'AGAG'],
            ['TATTCA', 'TTATAA', 'GTGGTA', 'TCAGCA', 'CTAGAG', 'TCCCAG'],
            ['AAAA', 'CCGC', 'TATT', 'AGAG'], # →
            ['ACGA', 'TCTT', 'TCCC', 'ACAA'], # ↓
            ['ACGA', 'TATT', 'TCAC', 'ACAA'], # ↘
            ['ACGA', 'TCAT', 'TACC', 'ACAA'], # ↗
            # Mutans
            ['AATA', 'ACTC', 'ATTT', 'AGTG'],
            ['CCGTTG','CAGGAG','TGACGT','GGGACG','TTTGAT','TGAAGC'],
            ['CCGTTG', 'CAGTAG', 'TGTCGT', 'GTGGCG', 'TTGGTT', 'TGAAGC'],
        ]

        for dna in dnas:
            self.client.post('/api/v1/mutant', { 'dna': dna }, format='json')

        # Check if cache it's working
        data = self.client.get('/api/v1/stats').data

        self.assertEqual(data['count_mutant_dna'], 0)
        self.assertEqual(data['count_human_dna'], 0)
        self.assertEqual(data['ratio'], 0)

        # Wait until the cache expires
        time.sleep(10)
        data = self.client.get('/api/v1/stats').data

        self.assertEqual(data['count_mutant_dna'], 3)
        self.assertEqual(data['count_human_dna'], 6)
        self.assertEqual(data['ratio'], 0.5)


