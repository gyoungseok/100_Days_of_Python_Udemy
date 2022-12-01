import csv

def getKey(item): # 정렬을 위한 함수
    return item[1] # 신경안써도됨

command_data = [] # 파일 읽어오기

with open('data/command_data.csv', 'r', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in spamreader:
        command_data.append(row)


# print(command_data)

command_counter = {}
for data in command_data: # list 타입을 dict 타입으로 변경
    if data[1] in command_counter.keys(): # 아이디가 이미 key값으로 변경되었을 때
        command_counter[data[1]] += 1 # 기존 아이디
    else:
        command_counter[data[1]] = 1 # 처음 나온 아이디
        
# print(command_counter)

dictlist = [] # dict를 list로 변경
for key, value in command_counter.items():
    temp = [key,value]
    dictlist.append(temp)
# print(dictlist)

sorted_list = sorted(dictlist, key=getKey, reverse=True)
print(sorted_list[:100])
    