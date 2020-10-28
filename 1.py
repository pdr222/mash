# Created by DXC Aka DuxkHack Aka DuckHack
# 28.10.20
# 10:28
print('Created by DXC')

import re

k = input('Paste JSON: ')

patern = r"ns\":\[{\"id\":\"......\",\"text\":\"(\w+|\d+)" # тут ахуеть какой патерн я в ахуе как я его написал
res = re.findall(patern, k) # тут применился

for i in range(len(res)):
	print('Задание №' + str(i + 1), ':', res[i] ) # а тут выводиться так что бы было ахуеть как красиво 