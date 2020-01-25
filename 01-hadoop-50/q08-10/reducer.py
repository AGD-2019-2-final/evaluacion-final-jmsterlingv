import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = 0
    promedio = 0
    p=0

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:

        key, val = line.split("\t")
        val = float(val)

        if key == curkey:
        	total = total + val
        	p += 1
        	promedio = total/p

        else:
            if curkey is None:
            	curkey=key
            	total=val
            	p = 1
            	promedio = total/p

            else:

                sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))

                curkey = key
                total = val
                p = 1
                promedio = total/p

    sys.stdout.write("{}\t{}\t{}\n".format(curkey, total, promedio))