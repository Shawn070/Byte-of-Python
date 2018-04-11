poem = '''\
Program is fun
when the work is done
if you wanna make your work also fun:
    use python!
'''

f = open('poem.txt', 'w')
f.write(poem)
f.close()

f = open('poem.txt')
# 默认以'r'打开
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
    # poem每行自带/n，print默认后面带一个/n，避免两个/

f.close()
