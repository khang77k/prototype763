import sys


def main(argv=None):
    argv = argv or sys.argv[1:]
    print('running', argv)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())

# rev 2ed7bb
