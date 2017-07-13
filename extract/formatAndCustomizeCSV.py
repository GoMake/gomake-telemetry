import csv
import sys
import os
os.chdir('outputs');

def create_csv():
  with open('logs.txt', 'r') as in_file:
  	stripped = (line.strip() for line in in_file)
  	lines = (line.split(",") for line in stripped if line)
  	with open(fileName, 'w') as out_file:
		  writer = csv.writer(out_file)
		  writer.writerows(lines)
		  print 'Results are available in ' + fileName 


def get_output_filename():
	global fileName
	fileName = input('Enter output csv name in single quotes with eg MAVERICK20160620 : ')
	try:
		if(fileName):
			fileName = fileName+ '.csv'
			print(fileName + ' will be used for charts')
	except ValueError:
		print 'Please provide a valid output file name.'


get_output_filename()
create_csv()