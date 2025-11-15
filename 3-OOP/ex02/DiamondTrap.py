from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Class representing a King, inheriting from Baratheon and Lannister."""

    def __init__(self, first_name: str) -> None:
        """Initialize the King with a first name."""
        Lannister.__init__(self, first_name)
        Baratheon.__init__(self, first_name)

    def set_eyes(self, eye_color: str) -> None:
        """Set the eye color of the King."""
        self.eyes = eye_color

    def set_hairs(self, hair_color: str) -> None:
        """Set the hair color of the King."""
        self.hairs = hair_color

    def get_eyes(self) -> str:
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self) -> str:
        """Get the hair color of the King."""
        return self.hairs


def main() -> None:
    """Main function to demonstrate the Stark class functionality."""
    Joffrey = King("Joffrey")
    print(Joffrey.__dict__)
    Joffrey.set_eyes("blue")
    Joffrey.set_hairs("light")
    print(Joffrey.get_eyes())
    print(Joffrey.get_hairs())
    print(Joffrey.__dict__)


if __name__ == "__main__":
    main()
