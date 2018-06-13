class MutantService:
    """
    Mutant Services
    """

    @staticmethod
    def is_mutant(adn):
        is_mutant = False
        adn = MutantService.convert_to_bidimensional(adn)

        return is_mutant

    @staticmethod
    def convert_to_bidimensional(adn):
        bidimensional = []
        for sequence in adn:
            bidimensional.append(list(sequence))

        return bidimensional
