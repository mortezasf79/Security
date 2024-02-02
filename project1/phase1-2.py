import math
import time
global guess

pasw = str(input('Input password: '))
chars = 'abcdefghijklmnopqrstuvwxyz' #only limeted myself to lowercase for simplllicity.
base = len(chars) + 1
size = int(input('enter size of password: '))
mod = int(input('enter mod number (1-standard, 2-with first character, 3-with part of pass): '))
firstChar = ''
if mod==2:
    firstChar = str(input('enter first character: '))
    size-=1
t1 = time.time()
#mod = input('please enter number of mod: ')
def cracker(pasw):
    guess = ''
    temp=0
    for i in range(size-1):
        temp += pow(base, i) 
    print(temp)
    tests = pow(base,size-1) + temp
    c = 0
    m = 0

    while True:
        y = tests
        while True:
            c = y % base
            m = math.floor((y - c) / base)
            y = m
            guess = chars[(c - 1)] + guess
            if m == 0:
                break
        guess = firstChar + guess
        print(guess)
        if guess == pasw:
            t2 = time.time()
            print('Got "{}" after {} tests'.format(guess, str(tests-pow(base,size-1) - temp + 1)))
            print('Time of crack password was {}'.format(t2 - t1))
            break
        else:
            tests += 1
            guess = ''

cracker(pasw)
input()