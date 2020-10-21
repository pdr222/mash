# Created by DXC Aka DuxkHack Aka DuckHack
# 21.10.2020
# 11.19
# пока я писал жту поеботу я послушал 2 раза все треки ган вест и половину треков лил кристала
# я не умею нормально програмровать и эта хуйня работает пиздец хуево
print("Created by DXC")
osnc = str(input('Raw data: '))
taskNum = osnc.split("\"taskNum\":")[-1].split('}]')[0]
taskNum = int(taskNum)
four = 1
for i in range(1, taskNum + 1):
    scnd = osnc.split('\"options\":')[i]
    thrd = (scnd[scnd.find("\"options\":") + 25:])
    four = thrd.find("\",\"co", four)
    if i != taskNum:
        last = (scnd[scnd.find("\"options\":") + 25:24 + four])
    else:
        last = (scnd[scnd.find("\"options\":") + 25:four - 38])
    print('Задание №' + str(i))
    print(last)

