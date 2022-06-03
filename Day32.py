#Small program that checks whether a number is divisible by certain values and checks its length in terms of characters.

my_number = 918652728452151

if my_number % 17 == 0 and len(str(my_number)) > 12 :
    print("Divisible by 17 and longer than 12 chars")
elif my_number % 13 == 0 and str(len(my_number)) > 10:
    print("Divisible by 13 and longer than 10 chars")
else:
    print("None of the above")