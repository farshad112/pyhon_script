##########################################################
## Text File Reader 
## Reads a text file and display lines in command prompt
##########################################################

def main():
	filepath = raw_input("Enter the path to the .txt file you want to read.\n")
	fh =open(filepath);
	for line in fh.readlines():
		print(line)

if __name__ == "__main__": main()