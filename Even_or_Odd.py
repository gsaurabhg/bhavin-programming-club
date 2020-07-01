#Pseudo code: this code determines if input number is even or odd
#ask user for the number
# If input is not an Integer, send error message 
#assign variable- NUM as answer,
#Find remainder when NUM/2
#If NUM mod 2=0:
#  "The Number is Even"
#If NUM mod 2 is not= 0
#  "the number is odd"

print('Hello! Please enter a number here so I can determine if its Even or Odd:  ')
try:
    NUM=int(input())
    if NUM%2==0:
        print('The number '+str(NUM)+' is Even')
    elif NUM%2!=0:
        print('The number '+(str(NUM))+' is Odd')
except ValueError:
    print('Please enter proper Integer value!')
