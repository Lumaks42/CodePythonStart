# C помощью методов работы со списками превратить "Don't panic!" в "on tap"

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4):							          # убераю последнии 4 объекта из plist, тем самым удаляю "nic!"
	plist.pop()
plist.pop(0)								              # убераю первую букву из списка
plist.remove("'")							            # нахожу и сношу апостров
plist.extend([plist.pop(), plist.pop()])	# меняю местами 2 объекта из конца списка
plist.insert(2, plist.pop(3))				      # переставляю пробел
new_phrase = ''.join(plist)					
print(plist)								        
print(new_phrase)							            # вывод новой фразы 
