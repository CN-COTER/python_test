def tidy_name(firstname,secondname):
	#输出整洁的姓名
	name = firstname + "  " + secondname
	return name.title()
tidy_name("liefu",'tuoersitai')


while True:
	print('\n Now tell me your name!')
	print('Enter "q" at any time to quit')
	f_name = input('First_name:')
	if f_name == 'q':
		break
	s_name = input('Second_name:')
	if s_name == 'q':
		break
	formatted_name = tidy_name(f_name,s_name)
	print(formatted_name)

def get_name(names):
	for name  in names:
		msg = '\nhello ' + name.title() + '\n'
		print(msg)
user_names=['gaga','tylor','leihana']
get_name(user_names)


复制列表或者修改列表
def copy_list(listA,listB):
	while listA:
		name=listA.pop()
		listB.append(name)
	for name in listB:
		print(name)
listC = ['AAAA', 'BBBBB','CCCCC']
listD = []
copy_list(listC,listD)




#引用列表时可以使用list[:]使用其副本进而不改变原列表
def copy_list(listA,listB):
	while listA:
		name=listA.pop()
		listB.append(name)
	for name in listB:
		print(name)
listC = ['AAAA', 'BBBBB','CCCCC']
listD = []
copy_list(listC[:],listD)
print(listC)



