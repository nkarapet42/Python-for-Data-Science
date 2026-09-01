from S1E9 import Character


class Baratheon(Character):
    """A class representing a member of House Baratheon."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a Baratheon character with a
        first name,alive status(Inherited from Character)
        family name, eye color, and hair color(Self).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"Vector: ('{self.family_name}',"
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """
        Docstring for __repr__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return self.__str__()

    def die(self) -> None:
        """Marks the character as dead by setting is_alive to False."""
        if self.is_alive:
            self.is_alive = False


class Lannister(Character):
    """A class representing a member of House Lannister."""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a Lannister character with
        a first name, alive status(Inherited from Character)
        family name, eye color, and hair color(Self).
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"Vector: ('{self.family_name}',"
                f"'{self.eyes}', '{self.hairs}')")

    def __repr__(self) -> str:
        """
        Docstring for __repr__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return self.__str__()

    def die(self) -> None:
        """Marks the character as dead by setting is_alive to False."""
        if self.is_alive:
            self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> 'Lannister':
        """
        Creates a new Lannister character.

        :param cls: Description
        :param first_name: Description
        :type first_name: str
        :param is_alive: Description
        :type is_alive: bool
        :return: Description
        :rtype: Lannister
        """
        return cls(first_name, is_alive)
