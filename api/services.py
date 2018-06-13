import numpy as np
class MutantService:
    """
    Mutant Services
    """

    @staticmethod
    def is_mutant(adn):
        adn = MutantService.convert_to_bidimensional(adn)

        return (MutantService.verify_horizontal(adn) or
            MutantService.verify_vertical(adn) or
            MutantService.verify_diagonal(adn))

    @staticmethod
    def convert_to_bidimensional(adn):
        bidimensional = []
        for sequence in adn:
            bidimensional.append(list(sequence))

        return bidimensional

    @staticmethod
    def verify_horizontal(adn):
        print(adn)
        return False

    @staticmethod
    def verify_vertical(adn):
        adn = np.transpose(adn)
        print(adn)
        return False

    @staticmethod
    def verify_diagonal(adn):
        x = len(adn[0])
        y = len(adn) -1
        diags = []
        for i in range(y * -1, 0):
            diags.append(np.diagonal(adn, i, -1, 0))
        for i in range(0, x):
            diags.append(np.diagonal(adn, i, -1, 0))

        print(diags)

        return False
