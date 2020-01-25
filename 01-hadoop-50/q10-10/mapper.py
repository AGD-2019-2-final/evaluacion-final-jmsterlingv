import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:

		numero=line.split('\t')[0]
		letra=line.split('\t')[1]


		#numero=int(numero)
				

		sys.stdout.write("{}\t{}\n".format(numero, letra))