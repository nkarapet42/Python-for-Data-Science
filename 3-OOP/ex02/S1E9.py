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
