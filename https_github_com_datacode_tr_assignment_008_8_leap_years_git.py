# -*- coding: utf-8 -*-
"""https://github.com/datacode-tr/Assignment-008-8-Leap-Years-.git

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ekxfjs0rD6gLMp0NOjsBCyPiM7OSR9ht
"""

number=int(input('enter  number'))
if number%4==0 and number%100==0 and number%400==0:
  print(number,'is leap year')
else:
    print(number,'is not leap year')