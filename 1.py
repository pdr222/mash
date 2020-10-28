# 18:00
# base on last script
# i work 5 hrs is pizdec nahuy
# Created by DXC Aka DuxkHack Aka DuckHack
# cdz auto gdz

print('Created by DXC')
import re
mPatern = r"answer\/multiple"
gPatern = r"answer\/groups"
sPatern = r"answer\/single"
oPatern = r"answer\/order"
aPatern = r"answer\/match"
DefPatern = r"\",\"text\":\"........................................................"
b = input('Paste JSON: ')
b = b.split('taskNum')

for i in range(len(b) - 1):
	if len(re.findall(gPatern, str(b[i]))) == 1:
		full = re.findall(DefPatern, str(b[i]))
		for lay in range(len(full)):
			xc = full[lay]
			full[lay] = xc[10:-1]
			full[lay] = full[lay].split('"')[0]
		print('Задание№', i + 1, full)

	elif len(re.findall(sPatern, str(b[i]))) == 1:
		SoloPatern = r"ns\":\[{\"id\":\"......\",\"text\":\"..........."
		full = re.findall(SoloPatern, str(b[i]))
		full = str(full).split("text\":\"")[1]
		full = full.split('"')[0]
		print('Задание№', i + 1, full)

	elif len(re.findall(mPatern, str(b[i]))) == 1:
		full = re.findall(DefPatern, str(b[i]))[0:3]
		for lay in range(len(full)):
			xc = full[lay]
			full[lay] = xc[10:-1]
			full[lay] = full[lay].split('"')[0]
		print('Задание№', i + 1, full)

	elif len(re.findall(oPatern, str(b[i]))) == 1: # какой вариант задачи
		full = re.findall(DefPatern, str(b[i])) # получает значения при помощт патерна
		for lay in range(len(full)): # кол во необходимых проходов те сколько в списке элементов
			xc = full[lay] # принимает значение переменной к которой будет применят действия
			full[lay] = xc[10:-1] # обрезает начало где хуита не нужная
			full[lay] = full[lay].split('"')[0] # обрезает по двоеточие
		print('Задание№', i + 1, full) # ну и вывод

	elif len(re.findall(aPatern, str(b[i]))) == 1:
		full = re.findall(DefPatern, str(b[i]))
		for lay in range(len(full)):
			xc = full[lay]
			full[lay] = xc[10:-1]
			full[lay] = full[lay].split('"')[0]
		print('Задание№', i + 1, full)
	
	else:
		print('Задание№', i + 1, 'if i stay robot i code it part')






#привет я в будущем я извиняюсь что накодил такую хуйню но она работает хотя бы