import sys
import numpy

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for filename in filenames:
            process(filename, action)

def process(filename, action):
        data = numpy.loadtxt(filename, delimiter=',')
    if action == '--min':
        values = data.min(axis=1)
    elif action == '--max':
        values = data.max(axis=1)
    elif action == '--mean':
        values = data.mean(axis=1)

    print(filename)
    for m in values:
        print(m)

main()


