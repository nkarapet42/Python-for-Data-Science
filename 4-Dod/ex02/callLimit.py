from typing import Any


def callLimit(limit: int):
    """Decorator that limits the number of calls to a function."""
    count = 0

    def callLimiter(function):
        """
        Inner function that checks the call count
        and calls the original function.
        """
        def limit_function(*args: Any, **kwds: Any):
            """
            Function that checks the call count
            and calls the original function.
            """
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter


def main() -> None:
    """Demonstrate callLimit decorator."""
    @callLimit(3)
    def f():
        """Function that prints 'f()'."""
        print("f()")

    @callLimit(1)
    def g():
        """Function that prints 'g()'."""
        print("g()")

    for _ in range(3):
        f()
        g()
    f()


if __name__ == "__main__":
    """Main entry point of the script."""
    main()
