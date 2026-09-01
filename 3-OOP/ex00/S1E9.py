from abc import ABC, abstractmethod


class Character(ABC):
    """Abstarct class representing a character"""

    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a character with a first name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self) -> None:
        """Does not implemented."""
        pass


class Stark(Character):
    """Class representing a Stark character"""
    def __init__(self, first_name: str, is_alive: bool = True) -> None:
        """Initializes a Stark character with a first name and alive status."""
        super().__init__(first_name, is_alive)

    def die(self) -> None:
        """Marks the character as dead by setting is_alive to False."""
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
    """Main entry point of the script."""
    main()
