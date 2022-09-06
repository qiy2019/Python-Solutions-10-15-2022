# -*- coding: utf-8 -*-
"""
Created on Tue Sep  6 16:28:12 2022

@author: qiy20
"""

high = 100;
low = 0;
mid = 0;
print("Please think of a number between 0 and 100!")
while (high > low):
    mid = (high + low) // 2
    print('Is your secret number ' + str(mid) + '?')
    s = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if (s == 'h'): high = mid
    elif (s == 'l'): low = mid
    elif (s == 'c'): break
    else: print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(mid))