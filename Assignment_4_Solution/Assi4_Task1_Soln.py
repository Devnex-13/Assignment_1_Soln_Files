try:
    f = open('sample.txt','r')
    for line in f.readlines():
        print(line)
    f.close()

except FileNotFoundError:
    print('The file \'sample.txt\' was not found.')
