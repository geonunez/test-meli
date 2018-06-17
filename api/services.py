# -*- coding: utf-8 -*-

import numpy as np

from .models import Human

class HumanService:
    """
    Human Services.
    """

    MUTATIONS = ['AAAA','TTTT', 'CCCC', 'GGGG']
    SEQUENCES_NEED_IT = 1

    def verify(self, dna):
        """
        Verifies if a dna is a mutant one or not.
        """
        s_dna = ''.join(dna)

        try:
            human = Human.objects.get(dna=s_dna)
        except Human.DoesNotExist:
            is_mutant = self.is_mutant(dna)
            human = Human.objects.create(dna=s_dna, is_mutant=is_mutant)

        return human

    def is_mutant(self, dna):
        """
        Challenge 1 algorithm.
        """
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
        """
        Converts a one dimensional list to a bidimensional list
        E.g: ['AB', 'CD'] → [['A', 'B'], ['C', 'D']]
        """
        bidimensional = []
        for sequence in dna:
            bidimensional.append(list(sequence))

        return bidimensional

    def _count_in_horizontal(self, dna):
        """
        Counts horizontal mutations sequence.
        """
        count = 0

        for sequence in dna:
            for mutation in self.MUTATIONS:
                count += sequence.count(mutation)

        return count

    def _count_in_vertical(self, dna):
        """
        Counts vertical mutations sequence.
        """
        count = 0
        dna = np.transpose(dna)

        for sequence in dna:
            for mutation in self.MUTATIONS:
                count += ''.join(sequence).count(mutation)

        return count

    def _count_in_diagonal(self, dna):
        """
        Counts diagonal mutations sequence.
        """
        count = 0
        hight = len(dna) - 1
        width = len(dna[0])

        # ↘ direction
        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(dna, i)).count(mutation)

        if count > self.SEQUENCES_NEED_IT:
            return count

        # ↗ direction
        dna = np.flip(dna, 0)

        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(dna, i)).count(mutation)

        return count

    def get_stats(self):
        """
        Gets the humans vs mutants stats.
        """
        humans = Human.objects.all()

        total = humans.count()
        count_mutant_dna = count_human_dna = ratio = 0

        if total > 0:
            for human in humans:
                count_mutant_dna += 1 if human.is_mutant else 0
            count_human_dna = total - count_mutant_dna

            # For me the right formula is count_mutant_dna / total
            ratio = (count_mutant_dna / count_human_dna if count_human_dna > 0 else 0)

        return { \
            'count_mutant_dna': count_mutant_dna, \
            'count_human_dna': count_human_dna, \
            'ratio': ratio \
        }
