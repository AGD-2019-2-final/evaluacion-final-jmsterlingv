import sys
#
#  >>> Escriba el codigo del mapper a partir de este punto <<<
#
if __name__ == "__main__":
	for line in sys.stdin:
		uno=line.split("   ")[0]
		dos=line.split("   ")[1]
		tres=line.split("   ")[2]
		
		#tres=int(tres)
		cuatro=tres.zfill(7)

		
		sys.stdout.write("{}\t{}\t{}\t{}\n".format(uno, cuatro, dos, tres))