import sys


def counter(user_input: str):
    """Counts the number of upper letters, lower letters, \
punctuation marks, digits, and spaces in the given text."""
    upper_count = lower_count = punct_count = spaces_count = digits_count = 0
    for n in user_input:
        if n.isupper():
            upper_count += 1
        elif n.islower():
            lower_count += 1
        elif n.isspace():
            spaces_count += 1
        elif n.isdigit():
            digits_count += 1
        else:
            punct_count += 1
    print(f"The text contains {len(user_input)} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punct_count} punctuation marks")
    print(f"{spaces_count} spaces")
    print(f"{digits_count} digits")


def main():
    """Main function to handle user input and call the counter function."""
    try:
        if len(sys.argv) == 1:
            user_input = input("What is the text to count?\n")
            counter(user_input)
        elif len(sys.argv) != 2:
            raise AssertionError("more than one argument is provided")
        else:
            counter(sys.argv[1])
    except Exception as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
