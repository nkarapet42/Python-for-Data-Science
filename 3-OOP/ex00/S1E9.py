from abc import ABC, abstractmethod


class Character(ABC):
    """
        An abstract base class representing a character in a story.
        Attributes:
        first_name (str): The first name of the character.
        is_alive (bool): A boolean indicating if the character is alive.

        Methods:
        die(): Does not implemented.
    """
    first_name: str
    is_alive: bool

    @abstractmethod
    def die(self) -> None:
        """Does not implemented."""
        pass


class Stark(Character):
    """
        A class representing a member of House Stark.
        Attributes Inherited from Character:
        first_name (str): The first name of the Stark character.
        is_alive (bool): A boolean indicating if the character is alive.

        Methods Inherited from Character:
        die(): Marks the character as dead by setting is_alive to False.
    """
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """
        Initializes a Stark character with a first name and alive status.
        Args:
        first_name (str): The first name of the Stark character.
        is_alive (bool): A boolean indicating if the character is alive.
                            Default is True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self) -> None:
        """
        Marks the character as dead by setting is_alive to False.
        """
        if self.is_alive:
            self.is_alive = False


def main() -> None:
    """Main function to demonstrate the Stark class functionality."""
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)


if __name__ == "__main__":
    main()
