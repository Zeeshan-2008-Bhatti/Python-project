my_list=[5,10,15,20,25]
print("first element:",my_list[0])
print("last element:",my_list[1])
print("All element:")
for item in my_list:
	print(item)

	print("Numbers greater than 10:")
	for item in my_list:
		if item > 10:
			print(item)