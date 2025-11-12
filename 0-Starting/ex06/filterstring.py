from ft_filter import ft_filter
import sys as s


def main():
    """Main function to filter strings\
based on length from command line arguments."""
    try:
        if (len(s.argv) != 3):
            return print("AssertionError: the arguments are bad")
        world_len = int(s.argv[2])
        worlds = s.argv[1].split(" ")
        print(list(ft_filter(lambda x: len(x) > world_len, worlds)))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
