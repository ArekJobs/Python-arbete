
from subprocess import call

with open('y_copy.py', 'w') as f:
    f.write('''
import random
i = random.randrange(10)

while (i<=10):
    print('6 * ',(i), '=',6 * i)

    if i >= 10:
        break
    i = i + 1
try:
  print("Here You go")
except:
  print("Something is wrong with the program")
else:
  print("The program is working")


            ''')
call(["python", "y_copy.py"])
