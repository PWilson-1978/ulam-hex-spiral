import turtle
import math as m
from datetime import datetime

'''
author: Paula Wilson, 20220529 
 
This routine will create a hexagon pattern with the primes all appearing on the upward diagonal radii.

At the end of the run, the start and stop time will display, along with the range used and the next number to start 
Also prints the list of primes from the range

If more than 250 is used for a range, the screen commands will stop, but the print will show. I found that on larger ranges, it seemed the screen commands were really slowing the process

Started with code from geekforgeeks, stackoverflow and possibly other sources

'''

print("Numbers separated by : - starting and number range like 5020:100")
cStr = input()

cNuml = cStr.split(':')

cNum = int(cNuml[0])
cNum2 = int(cNuml[1])
cNumR = cNum2
cNum2 += cNum

print('cNum: ', cNum)
print('cNum2: ', cNum2)
print('cNumR: ', cNumR)

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time is :", current_time)

############

# Start a work Screen
ws = turtle.Screen()

# Define a Turtle Instance
t = turtle.Turtle()
 
# executing loop 6 times for 6 sides
t.penup()

###########
def level_display(hex_info):
    

    global ccnt
    for i in range(6):
        cur_num = nlst[i]
        ccnt += 1
        t.penup()
        #t.width(ccnt/1000+1)
        #t.forward(ccnt*2)

        #Turn left the turtle by 300 degrees
        if hex_info == True:
            tempcnt = adjust_len(cNum)
            #print('Length of starting value: ', tempcnt)
            if i == 1:
               t.goto(6.19,30.73)
               t.left(30)
            else:
              t.left(60)
        else:
           t.left(60)
        
        prime_id = 0
        if isPrime(cur_num) == True:
            t.color('blue')
            #t.color('#3c79b8') #smokey blue hex
            prime_vals.append(cur_num)
            prime_id = 1
        else:
            t.color('grey')

        if ccnt < 250:
            if ccnt > 7:
                t.write(cur_num)        

            if i == 5:
                t.penup()
                t.forward(ccnt*2)
            else:
                t.width(ccnt+5/1000+1.5)
                t.forward(ccnt*2)

        #if prime_id == 1 or (ccnt > 6 and ccnt < 200):
        if cur_num % 6 in (1,5):
            print('pos: ', t.pos(), 'i: ',i, 'num: ', cur_num, 'prime: ', prime_id)
#########
def adjust_start(value):
    #adjust starting number to make sure the primes appear on the upward diagonals

    cNumT = value % 6
    print ('Initial starting point: ', cNumT)

    if cNumT != 2:
        for z in range(6):
            value -= 1
            if value % 6 == 2:
                return value
    return 0
########
def adjust_len(myval):

    mylen = len(str(myval))
    mynew = []
    mynew2 = ''
    for i in range(mylen):
        if i == 0:
            mynew.append('1')
        else:
            mynew.append('0')
    mynew2 = mynew2.join(mynew)
    return int(mynew2)
########
def isPrime(value):

    # if the value is value is evenly divisible by 2 or has 5 for the last digit
    if value % 2 == 0 or int(repr(value)[-1]) == 5:
        return False   

    if value % 6 in (1,5):
         testval = m.sqrt(value)

         #print('value: ', value, 'sqrt: ', testval)
         #for (i = 2; i < m.sqrt(value); i++):
         if testval > 2:
             for i in range(2,int(testval)+1):
                 if value % i == 0:
                     return False

             return True
    return False
###################
# Main work

# adjust the start value so the primes will appear on the two upward diagonals
rNum = adjust_start(cNum)
if rNum != 0:
    cNum = rNum

print ('Starting point: ', cNum % 6)

tcnt = cNum
ccnt = 0
prime_vals = []
hinfo = False

print('cNum: ', cNum, '; cNumR/6: ', int(cNumR/6))

# Add a few numbers to the start to keep from the crunch

for x in range(int(cNumR/6)):
     #print('Current iteration value: ', x, 'of ',int(cNumR/6))
     nlst = []
     if tcnt == cNum:
         hinfo = True

     for j in range(6):
         tcnt += 1
         nlst.append(tcnt)

     if nlst[-1] <= cNum2:
         bogus = level_display(hinfo)
     else:
       break

     hinfo = False
#####################

now = datetime.now()
now_time = now.strftime("%H:%M:%S")
print(prime_vals)

print("Start Time was  :", current_time)
print("End Time was :", now_time)
print('Range was: ', cNum, ' with range: ', cNumR)
print ('Next num: ', cNum2+1)
print ('Starting point: ', cNumT)


