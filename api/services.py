import numpy as np
class MutantService:
    """
    Mutant Services
    """
    MUTATIONS = ['AAAA','TTTT', 'CCCC', 'GGGG']
    SEQUENCES_NEED_IT = 1

    def is_mutant(self, adn):
        mutations_count = self._count_in_horizontal(adn)


        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True

        adn = self._convert_to_bidimensional(adn)
        mutations_count += self._count_in_vertical(adn)

        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True

        mutations_count += self._count_in_diagonal(adn)

        if (mutations_count > self.SEQUENCES_NEED_IT):
            return True
        else:
            return False

    def _convert_to_bidimensional(self, adn):
        bidimensional = []
        for sequence in adn:
            bidimensional.append(list(sequence))

        return bidimensional

    def _count_in_horizontal(self, adn):
        count = 0

        for sequence in adn:
            for mutation in self.MUTATIONS:
                count += sequence.count(mutation)

        return count

    def _count_in_vertical(self, adn):
        count = 0
        adn = np.transpose(adn)

        for sequence in adn:
            for mutation in self.MUTATIONS:
                count += ''.join(sequence).count(mutation)

        return count

    def _count_in_diagonal(self, adn):
        count = 0
        hight = len(adn) - 1
        width = len(adn[0])

        # ↘
        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(adn, i)).count(mutation)

        if count > self.SEQUENCES_NEED_IT:
            return count

        # ↗
        adn = np.flip(adn, 0)

        for i in range(hight * -1, width):
            for mutation in self.MUTATIONS:
                count += ''.join(np.diagonal(adn, i)).count(mutation)

        print(count)

        return count
