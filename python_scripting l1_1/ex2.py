import sys

def isWhiteLine(instring):
    if len(instring.strip().strip('\t')) == 0:
        return True
    else:
        return False

def printdoc(fil):

    with open(fil, 'r') as fl:
        for line in [l.strip('\n') for l in list(fl)]:
            if not isWhiteLine(line):
                print(line)

def main(cmdline=False):


    if cmdline:
        inputfile = sys.argv[1]

    else:
        inputfile = input('Enter file')
    printdoc(inputfile)

if __name__ == '__main__':
    main(cmdline=False)

