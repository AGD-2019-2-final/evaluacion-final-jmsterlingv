import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = 0
    totalmin = 0

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key, val = line.split('\t')
        #val = int(val)

        if key == curkey:
        	total = max(val, total)
        	totalmin = min(val, totalmin)
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, totalmin))

            curkey = key
            total = val
            totalmin = val

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, totalmin))