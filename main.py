import random
password = list('abcdefghijklmnopqrstuvwxyz')
password = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
random.shuffle(password)
password = ''.join([random.choice(password) for x in range(11)])
print (password) # шкиd69#&
