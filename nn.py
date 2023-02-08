import fileinput

for line in fileinput.input(files='y.txt'):
    print(line)

f = open("y.txt", "a")
f.write("yes")
f.close()

f = open("y.txt", "r")
print(f.read())



from subprocess import call

with open('y_copy.py', 'w') as f:
    f.write('''
yes = True
while yes:
    print('hey')

            ''')
call(["python", "y_copy.py"])
