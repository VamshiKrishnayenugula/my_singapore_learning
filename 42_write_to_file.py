names = ['John Kelly', 'Moses Nkosi', 'Joseph Marley']

with open('name.csv','w') as f:
    for name in names:
        f.write(name)
        f.write('\n')


with open('name.csv','r') as fr:
    print(fr.read())