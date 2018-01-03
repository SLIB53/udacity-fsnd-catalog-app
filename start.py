#! /usr/bin/env python3

import argparse
import sys
import start_database
import start_http_server


def main():
    parser = argparse.ArgumentParser(prog='start')
    parser.add_argument('--resolve',
                        default='false',
                        help="Fix issues before running. (Options: %s)"
                             % "on, off, true, false")

    arg_resolve = parser.parse_args().resolve.lower()

    if not start_database.check():
        if arg_resolve == 'false' or arg_resolve == 'off':
            print("Quitting.")
            sys.exit(1)
        elif arg_resolve == 'true' or arg_resolve == 'on':
            print("Resolving...")
            start_database.setup()

            if not start_database.check():
                print("Failed to resolved. Quitting")
                sys.exit(1)
        else:
            print("Invalid option passed with --resolve. Quitting")
            sys.exit(1)

    print("Starting HTTP server...")
    start_http_server.start()


if __name__ == '__main__':
    main()
