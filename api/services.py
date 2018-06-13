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
        fadn = np.flip(adn, 0)
        diags = []
        fdiags = []

        # X
        for i in range((len(adn) -1) * -1, 0):
            diags.append(np.diagonal(adn, i))
            fdiags.append(np.diagonal(fadn, i))

        # Y
        for i in range(len(adn[0])):
            diags.append(np.diagonal(adn, i))
            fdiags.append(np.diagonal(fadn, i))

        print(fdiags)

        return False
