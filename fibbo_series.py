########################################################
# Fibbonochi series calculator
# Author: Farshad
########################################################

def main():
	limit = input("How many member do you want me to calculate:\t")
	a=1;
	b=0;
	count=1;
	while  count<= limit:
		a, b = b, a+b
		print str(b)
		count = count+1 
	else:
		print "\nComputation complete......."	

if __name__ == "__main__": main();		
	