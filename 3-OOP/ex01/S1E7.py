from S1E9 import Character


class Baratheon(Character):
    """
        A class representing a member of House Baratheon.
        Attributes Inherited from Character:
        first_name (str): The first name of the Baratheon character.
        is_alive (bool): A boolean indicating if the character is alive.

        Additional Attributes:
        family_name (str): The family name of the Baratheon character.
        eyes (str): The eye color of the Baratheon character.
        hairs (str): The hair color of the Baratheon character.

        Methods Inherited from Character:
        die(): Marks the character as dead by setting is_alive to False.
    """

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :type first_name: str
        :param is_alive: Description
        :type is_alive: bool
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.familty_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"Vector: ('{self.familty_name}',"
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
        """
        Marks the character as dead by setting is_alive to False.
        """
        if self.is_alive:
            self.is_alive = False


class Lannister(Character):
    """
        A class representing a member of House Lannister.
        Attributes Inherited from Character:
        first_name (str): The first name of the Lannister character.
        is_alive (bool): A boolean indicating if the character is alive.

        Additional Attributes:
        family_name (str): The family name of the Lannister character.
        eyes (str): The eye color of the Lannister character.
        hairs (str): The hair color of the Lannister character.

        Methods Inherited from Character:
        die(): Marks the character as dead by setting is_alive to False.

        Class Methods:
        create_lannister(): Creates and returns a new Lannister instance.
    """
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Docstring for __init__

        :param self: Description
        :param first_name: Description
        :type first_name: str
        :param is_alive: Description
        :type is_alive: bool
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.familty_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def __str__(self) -> str:
        """
        Docstring for __str__

        :param self: Description
        :return: Description
        :rtype: str
        """
        return (f"Vector: ('{self.familty_name}',"
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
        """
        Marks the character as dead by setting is_alive to False.
        """
        if self.is_alive:
            self.is_alive = False

    @classmethod
    def create_lannister(cls, first_name: str,
                         is_alive: bool = True) -> 'Lannister':
        """
        Docstring for create_lannister

        :param cls: Description
        :param first_name: Description
        :type first_name: str
        :param is_alive: Description
        :type is_alive: bool
        :return: Description
        :rtype: Lannister
        """
        return cls(first_name, is_alive)


def main() -> None:
    """Main function to demonstrate the Stark class functionality."""
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("---")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)
    print("---")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name : {Jaine.first_name, type(Jaine).__name__},"
          f" Alive : {Jaine.is_alive}")


if __name__ == "__main__":
    main()
