import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
    for line in sys.stdin:
        uno = line.split('   ')[0]
        dos = line.split('   ')[1]
        tres = int(line.split('   ')[2])
        tres_format = "{:03.0f}".format(tres)
        sys.stdout.write("{}\t{}\t{}\t{}\n".format(uno,tres_format,dos,tres))