


def go_to_next_part():
    typed_stuff = input('Hit enter to print what you type, and to go to the next part. ')
    print(typed_stuff)




print('PART ONE!')
integer = 10002
print(f'(This is a string, I can put whatever in here) This is an integer: {integer}')


float = 1586.346753674739868468
print(f'This is a float number: {float}')

go_to_next_part()wer
print('PART TWO!')


list_of_stuff = [1, 5, 5, 'qsdkjkasgiwsdngjseaj;sflnasbadjgn;shasdfsfgsfgjkla']
print(list_of_stuff)

boolean = True
print(boolean)


go_to_next_part()
print('PART THREE')

number1 = integer + float
print(number1)
number2 = integer - float
print(number2)
number3 = integer * float
print(number3)
number4 = integer / float

print('The end!')
thought = input('What did you think of this?: good, bad , ok, HORRIBLE!, AMAZING! ')

if thought == 'good':
    print('Thanks, bye nerd')
elif thought == 'bad':
    print('AWW, that is to bad')
elif thought == 'ok':
    print('Ok, Bye')
elif thought == 'HORRIBLE!':
    print('NOT AS HORRIBLE AS YOU OR YOUR MOM! GET OUT OF HERE!')
elif thought == 'AMAZING!':
    print('THANKS! I HOPE YOU COME BACK TO THE NEXT TUTORIAL!')
else:
    print('Uhmmmmmmmmmmmmmmmmmm ok.')



# create a function.
def go_to_next_part():
    # create a string which is the stuff you type in the console.
    typed_stuff = input('hit enter to print what you type, and to go to the next part. ')
    # print the variable out into the console.
    print(typed_stuff)






print('PART ONE!')
integer = 10045678
#wrong: print('This is an integer: ' + str(integer))
# right: VVV
# The f at the start allows the use of curley brackets which will convert any variable into a string.
print(f'(This is a string, i can put whatever in here) This is an integer: {integer}')

# float/unified number is a number with decimals.
float_aka_unified_number = 16896.38375836734883496734876926
print(f'This is a float number: {float_aka_unified_number}')

# Call the go_to_next_part function to use the code in it.
go_to_next_part()
print('PART TWO!')

# Create a list with 4 objects in it. (A list has brackets around it.)
list_of_stuff = [1, 5, 5, '2kejj2m1r3mgkl24u890yuo35nhui35u8hp;;k,].']
print(list_of_stuff)

# Create a variable which is a boolean aka true or false.
boolean = True
print(boolean)

go_to_next_part()
print('PART THREE!')

number1 = integer + float_aka_unified_number
print(number1)
number2 = integer - float_aka_unified_number
print(number2)
number3 = integer * float_aka_unified_number
print(number3)
number4 = integer / float_aka_unified_number
print(number4)

print('The end!')
thought = input('What did you think of this?: good, bad, ok, HORRIBLE!, AMAZING! ')
# If the thought is 'good' then print('Thanks, cya!').
if thought == 'good':
    print('Thanks, cya on the: if game!')
# Basically: if its not 'good', and it is 'bad' then print('Aww that is to bad.').
elif thought == 'bad':
    print('Aww that is to bad.')
elif thought == 'ok':
    print('Ok, bye')
elif thought == 'HORRIBLE!':
    print('NOT AS HORRIBLE AS YOU! GET OUT OF HERE!')
elif thought == 'AMAZING!':
    print('AWESOME thank you so much. I have extra practice thing for the lesson I hope you come.')
# If none of those other things do this.@else:
    print('Uhmmmmmm ok.')
exit()

