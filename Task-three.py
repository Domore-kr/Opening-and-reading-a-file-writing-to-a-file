import os

way = os.path.join(os.getcwd(), 'text')
lst = []
for i in os.listdir(way):
    if i.endswith('.txt'):
        with open(os.path.join(os.getcwd(), 'text', i)) as read_list:
            dct = {'Имя файла': i, 'Данные файла': read_list.readlines()}
            dct['Количество строк'] = len(dct['Данные файла'])
            lst.append(dct)

with open('sorted_text.txt', 'a', encoding='utf-8') as sorted_text:
    for i in sorted(lst, key=lambda x: x['Данные файла'], reverse=True):
        sorted_text.write(i['Имя файла'])
        sorted_text.write('\n')
        sorted_text.write(str(i['Количество строк']))
        sorted_text.write('\n')
        for a in i['Данные файла']:
            sorted_text.write(str(a).strip())
            sorted_text.write('\n')
