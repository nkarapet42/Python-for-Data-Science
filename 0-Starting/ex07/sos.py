import sys as s


NESTED_MORSE = {
    'A': '.-',     'B': '-...',   'C': '-.-.',
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.',
    ' ': '/'
}


def sos(string) -> None:
    """Convert a string to Morse code and print it."""
    for char in string:
        if not char.isalpha() and not char.isnumeric() and char != ' ':
            raise ValueError("AssertionError: the arguments are bad")
    morse_code = ' '.join(NESTED_MORSE[char.upper()] for char in string)
    print(morse_code)


def main() -> None:
    """Main function to handle command line arguments and call sos function."""
    try:
        if len(s.argv) != 2:
            return print("AssertionError: the arguments are bad")
        sos(s.argv[1])
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
