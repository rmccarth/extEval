import pandas

def getURL():

	data = pandas.read_csv("urls.csv", header=0)  #Create pandas DataFrame by reading top-1m sites csv
	col_a = list(data.number)		      
	col_b = list(data.url[0:5001])		      #grab URL column and first 5000 links from DataFrame. This executiion was done in segments by team members.
	return col_b				      

def main():
	getURL()

main()
