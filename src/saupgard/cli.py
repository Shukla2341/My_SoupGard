import argparse

from saupgard import __version__


def main():
    parser = argparse.ArgumentParser(
        description="SoupGuard CLI"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=__version__
    )

    parser.add_argument(
        "--name",
        default="Developer"
    )

    args = parser.parse_args()

    print(f"Welcome {args.name}!")
    print("SoupGuard is running successfully.")


if __name__ == "__main__":
    main()