import csv

def parse_csv(file):
	data_set = dict()
	with open(file) as csv_file:
		content = csv_file.readlines()
		for line in content:
			line = line.strip()
			each_pair=line.split(',')
			#print(each_pair)
			data_set[each_pair[0]] = each_pair[1]
	return data_set
	#print(data_set)
#parse_csv('test.csv')