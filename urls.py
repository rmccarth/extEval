import pandas

def getURL():

	data = pandas.read_csv("urls.csv", header=0)  #Create pandas DataFrame by reading top-1m sites csv
	col_a = list(data.number)		      
	col_b = list(data.url[0:9])		      #grab URL column and first 9 links from DataFrame
	return col_b				      #THIS METHOD STILL NEEDS TO VISIT EACH LINK AND PULL FIRST 5 LINKS AND ADD IT TO A LIST ELEMENT TO RETURN

def main():
	getURL()

main()
