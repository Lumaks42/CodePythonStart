# Вывести кол-во гласных букв в предложекние введеных пользователем.
vowels = ['a', 'e', 'i', 'o', 'u']                        # список гласных букв
word = input("Provide a word to search for vowels: ")     # запрос предложения, слова
found = {}                                                # словарь

found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0

for letter in word:                                       # перебор букв в слове
	if letter in vowels:                                    # если буква глассная
		found[letter] += 1                                    # +1 буква

for k, v in sorted(found.items()):                        # ключ и значение 
	print(k, 'was found', v, 'time(s).')                    # буква ее кол-во
