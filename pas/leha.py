import random 
word = 'qwertyuiopasdfghjklzxcvbnm'
password_text = list(word)
random.shuffle(password_text)
test = ''.join([random.choice(password_text) for x in range (5)])
print (test)