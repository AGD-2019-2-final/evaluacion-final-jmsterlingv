import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == '__main__':

    

    ##
    ## cada linea de texto recibida es una
    ## entrada clave \tabulador valor
    ##
    for line in sys.stdin:
        uno,tres_format,dos,tres = line.split("\t")
        tres=int(tres)
        
        sys.stdout.write("{}   {}   {}\n".format(uno, dos, tres))

        