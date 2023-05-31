word = "bottels"
for lemonade_num in range(99, 0, -1):
	print(lemonade_num, word, "of lemonade on the wall.")
	print(lemonade_num, word, "of lemonade.")
	print("Take one down.")
	print("Pass it around.")
	if lemonade_num == 1:
		print("No more bottels of beer on the wall.")
	else:
		new_num = lemonade_num - 1
		if new_num == 1:
			word = "bottle"
		print(new_num, word, "of lemonade on the wall.")
	print()
