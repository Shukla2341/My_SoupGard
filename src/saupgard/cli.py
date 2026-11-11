#from typing import Self
import argparse

from saupgard import __version__

from saupgard.platform_check import check_platform

from saupgard.banner import get_banner

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
    
    print(check_platform())
    print(get_banner())

    print(f"Welcome {args.name}!")
    print("SoupGuard is running successfully.")


if __name__ == "__main__":
    main()