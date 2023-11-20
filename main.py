from input import inputting, validation
from txt import txt, func

menu = ''
lst = []
for i in func.keys():
    menu += f'{i}) {func[i]['name']}\n'

print(txt['version'])
print()
print(txt['hi'])
print(txt['list_input'])
inp = inputting('Ввод: ')
while inp != 'ьъё':
    lst.append(inp)
    inp = inputting('Ввод: ')
print(txt['choosing'])
print(menu)
choose = validation([x for x in func.keys()])
print(func[choose]['function'].apply_to_list(lst))
