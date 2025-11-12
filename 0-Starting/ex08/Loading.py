import os as s


def ft_tqdm(lst: range) -> None:
    """A simple implementation of a progress bar similar to tqdm."""
    total = len(lst)
    columns = s.get_terminal_size().columns
    bar_size = columns - 36 - (len(str(total)) * 2 + 2)
    for i, elem in enumerate(lst, start=1):
        percent = i / total
        filled = int(bar_size * percent)
        bar = '█' * filled + ' ' * (bar_size - filled)
        progress = int(percent * 100)
        print(f"\r{progress:3d}%|{bar}| {i}/{total}", end='', flush=True)
        yield elem
    print()


def main() -> None:
    """Main function to demonstrate the ft_tqdm progress bar."""
    for elem in ft_tqdm(range(333)):
        pass


if __name__ == "__main__":
    main()
