import sys as s


def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n\n\
Return a list of items from iterable for which function(item) is true.
If function is None, return the items that are true."""
    if function is None:
        return [item for item in iterable if item]
    return [item for item in iterable if function(item)]


def main():
    """Main function to filter strings\
based on length from command line arguments."""
    try:
        if (len(s.argv) != 3):
            return print("AssertionError: the arguments are bad")
        word_len = int(s.argv[2])
        words = s.argv[1].split(" ")
        print(list(ft_filter(lambda x: len(x) > word_len, words)))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
