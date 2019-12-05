from brainfuck import Brainfuck
import argparse
import sys

NO_LOGGING = 0
LOG_TO_STDOUT = 1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--log', nargs='?', default=NO_LOGGING, const=LOG_TO_STDOUT)

    args = parser.parse_args()
    
    if args.log:
        if args.log == LOG_TO_STDOUT:
            logging.basicConfig(
                stream=sys.stdout,
                format='%(asctime)s: %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S',
                level=logging.INFO)
        else:
            logging.basicConfig(
            filename='{}'.format(args.log),
            filemode='w',
            format='%(asctime)s: %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.INFO)


    brainfuck = Brainfuck("++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>123+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.")

    try:
        brainfuck.run()
    except KeyboardInterrupt:
        pass
