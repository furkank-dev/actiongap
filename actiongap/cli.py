import argparse
import sys

from actiongap import __version__


def main(argv=None):
    parser = argparse.ArgumentParser(prog="actiongap")
    parser.add_argument("--version", action="version", version=__version__)
    sub = parser.add_subparsers(dest="command")

    scan = sub.add_parser("scan", help="scan a repo's workflows")
    scan.add_argument("repo", help="owner/repo")

    args = parser.parse_args(argv)

    if args.command == "scan":
        print(f"scan {args.repo}: not implemented yet")
        return 1

    parser.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
