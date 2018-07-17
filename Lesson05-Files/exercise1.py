f = open('note.txt', 'w')
date = input('輸入日期:')
event = input('輸入事件:')
description  = input('輸入心得:')
f.write(date + '\n')
f.write(event + '\n')
f.write(description)
f = open('note.txt', 'r')
print(f.read())
f.close()







