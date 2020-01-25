import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		letra=line.split('   ')[0]
		fecha=line.split('   ')[1]
		numero=line.split('   ')[2]

		numero=int(numero)
		entero=str(numero).zfill(5)

		#numero=int(numero)

		sys.stdout.write("{}\t{}\t{}\t{}\n".format(entero, letra, fecha, numero))