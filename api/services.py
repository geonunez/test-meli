# -*- coding: utf-8 -*-

import numpy as np

class HumanService:
    """
    Mutant Services
    """
    MUTATIONS = ['AAAA','TTTT', 'CCCC', 'GGGG']
    SEQUENCES_NEED_IT = 1

    def is_mutant(self, dna):
        mutations_count = self._count_in_horizontal(dna)


        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True

        dna = self._convert_to_bidimensional(dna)
        mutations_count += self._count_in_vertical(dna)

        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True

        mutations_count += self._count_in_diagonal(dna)

        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True
        else:
            return False

    def _convert_to_bidimensional(self, dna):
        bidimensional = []
        for sequence in dna:
            bidimensional.append(list(sequence))

        return bidimensional

    def _count_in_horizontal(self, dna):
        count = 0

        for sequence in dna:
            for mutation in self.MUTATIONS:
                count += sequence.count(mutation)

        return count

    def _count_in_vertical(self, dna):
        count = 0
        dna = np.transpose(dna)

        for sequence in dna:
            for mutation in self.MUTATIONS:
                count += ''.join(sequence).count(mutation)

        return count

    def _count_in_diagonal(self, dna):
        count = 0
        hight = len(dna) - 1
        width = len(dna[0])

        # ↘
        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(dna, i)).count(mutation)

        if count > self.SEQUENCES_NEED_IT:
            return count

        # ↗
        dna = np.flip(dna, 0)

        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(dna, i)).count(mutation)

        return count
