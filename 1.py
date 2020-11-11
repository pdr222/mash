# 18:00
# jsonase on last script
# i work 5 hrs is pizdec nahuy
# Created jsony DXC Aka DuxkHack Aka DuckHack
# cdz auto gdz
import re

print('Created by Duxk')
mPatern = r"answer\/multiple"
gPatern = r"answer\/groups"
sPatern = r"answer\/single"
oPatern = r"answer\/order"
aPatern = r"answer\/match"
DefPatern = r"\",\"text\":\"..........................................................................................."
json = input('Paste ur json')
json = json.split('taskNum')

for i in range(len(json) - 1):
    if len(re.findall(gPatern, str(json[i]))) == 1:
        full = re.findall(DefPatern, str(json[i]))
        for lay in range(len(full)):
            xc = full[lay]
            full[lay] = xc[10:-23]
            full[lay] = full[lay].split('"')[0]
        print('Задание№', str(i + 1) + ':', ((str(full)[1:-1]).replace("'", '')).replace(',', ''))

    elif len(re.findall(sPatern, str(json[i]))) == 1:
        SoloPatern = r"ns\":\[{\"id\":\"......\",\"text\":\"............................................................................................."
        full = re.findall(SoloPatern, str(json[i]))
        full = str(full)[28:-1]
        full = full.split('"')[1]
        print('Задание№', str(i + 1) + ':', ((str(full))))

    elif len(re.findall(mPatern, str(json[i]))) == 1:
        full = re.findall(DefPatern, str(json[i]))[0:3]
        for lay in range(len(full)):
            xc = full[lay]
            full[lay] = xc[10:-1]
            full[lay] = full[lay].split('"')[0]
        print('Задание№', str(i + 1) + ':', ((str(full)[1:-1]).replace("'", '')).replace(',', ''))

    elif len(re.findall(oPatern, str(json[i]))) == 1:
        full = re.findall(DefPatern, str(json[i]))
        for lay in range(len(full)):
            xc = full[lay]
            full[lay] = xc[10:-1]
            full[lay] = full[lay].split('"')[0]
        print('Задание№', str(i + 1) + ':', ((str(full)[1:-1]).replace("'", '')).replace(',', ''))

    elif len(re.findall(aPatern, str(json[i]))) == 1:
        full = re.findall(DefPatern, str(json[i]))
        for lay in range(len(full)):
            xc = full[lay]
            full[lay] = xc[10:-1]
            full[lay] = full[lay].split('"')[0]
        print('Задание№', str(i + 1) + ':', ((str(full)[1:-1]).replace("'", '')).replace(',', ''))

    else:
        print('Задание№', str(i + 1) + ':', 'IS PIZDOS I CANT CODE IT')
print('Duxk что ты сделал')
