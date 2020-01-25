import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    curkey = None
    total = 0
    cuenta = 0

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##

    for line in sys.stdin:
    	if cuenta < 6:
    		entero, key, fecha, val = line.split("\t")

    		val=int(val)

    		sys.stdout.write("{}\t{}\t{}\n".format(key, fecha, val))

    		cuenta += 1

        
        #sys.stdout.write("{}\t{}\n".format(curkey, total))