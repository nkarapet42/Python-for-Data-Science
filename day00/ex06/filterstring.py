from ft_filter import ft_filter
import sys


def main():
    try:
        if (len(sys.argv) != 3):
            return print("AssertionError: the arguments are bad")
        world_len = int(sys.argv[2])
        worlds = sys.argv[1].split(" ")
        print(list(ft_filter(lambda x: len(x) > world_len, worlds)))
    except Exception:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
