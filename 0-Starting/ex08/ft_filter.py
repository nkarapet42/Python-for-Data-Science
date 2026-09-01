
def ft_filter(function, iterable):
    """filter(function or None, iterable) --> filter object\n\n\
Return an iterator yielding those items of iterable for which function(item)\n\
is true. If function is None, return the items that are true."""
    for item in iterable:
        if function is None:
            if item:
                yield item
        elif function(item):
            yield item


def main():
    """Main function."""
    try:
        test_list = ["hello", "world", "this", "is", "a", "test"]
        result = ft_filter(lambda x: len(x) > 3, test_list)
        print(list(result))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
