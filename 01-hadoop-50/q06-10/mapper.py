import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#

if __name__ == "__main__":
	for line in sys.stdin:
		uno=line.split('   ')[0]
		#dos=line.split('\t')[1]
		tres=line.split('   ')[2]

		tres = float(tres)

		sys.stdout.write("{}\t{}\n".format(uno, tres))