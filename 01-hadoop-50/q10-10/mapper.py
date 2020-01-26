import sys
#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		num = int(line.split('\t')[0])
		num_format = "{:03.0f}".format(num)
		letras = line.split('\t')[1]
		letras = letras.rstrip('\r\n')
		letras_sep = letras.split(',')

		for i in range(len(letras)):

			sys.stdout.write("{}\t{}\n".format(str(letras[i]),num_format))