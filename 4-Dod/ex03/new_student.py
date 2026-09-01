import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generate a random student ID consisting of 15 lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """
    Class representing a student with name, surname,
    active status, login, and student ID.
    """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(default_factory=generate_id, init=False)

    def __post_init__(self):
        """Post-initialization to generate the login."""
        self.login = f"{self.name[0]}{self.surname}"


def main():
    """Demonstrate the Student class."""
    try:
        student = Student(name="Edward", surname="agle")
        print(student)
        student = Student(name="Edward", surname="agle", active=False)
        print(student)
        student = Student(name="Edward", surname="agle",
                          active=False, login="custom_login")
    except TypeError as e:
        print(f"Error: {e}")
    try:
        student = Student(name="Edward", surname="agle", id="custom_id")
    except TypeError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
