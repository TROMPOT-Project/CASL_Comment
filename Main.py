# coding: utf-8

input_data = []

##### Input Data #####
while(True):
	data = input()
	if data != "unchi":
		input_data.append(data)
	else:
		break

print()

for row_str, count in zip(input_data, range(len(input_data))):
	row_data = row_str.split("\t")
	try:
		label = row_data[0]
		order = row_data[1]
		operand = row_data[2]
	except:
		pass

##### Select Mode #####
	if count == 0:
		mode = "Start"
	elif label == "MAIN" or label == "":
		mode = "Main"
	elif mode == "Start":
		mode = "Data"

##### Main #####
	if mode == "Start":
		print(row_str)
	elif mode == "Data":
		if order == "DC":
			print(row_str + "\t;(" + label + ") <= " + operand)
		elif order == "DS":
			print(row_str + "\t;(" + label + ") <= " + operand + "word")
	elif mode == "Main":
		try:
			register = operand.split(",")[0]
			address = operand.split(",")[1]
		except:
			pass

		if order == "LD":
			print(row_str + "\t;" + register + " <= (" + address + ")")


	print(mode)
	print()

