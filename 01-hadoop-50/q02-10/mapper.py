import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		amount=line.split(',')[4]
		purpose=line.split(',')[3]

		sys.stdout.write("{}\t{}\n".format(purpose, amount))