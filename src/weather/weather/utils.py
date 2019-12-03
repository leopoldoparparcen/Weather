import csv


def csvtolist (file):
	reader = csv.reader(file)
	data = list(reader)

	return data
