





# ask your name, and create a variable called name
# and it will set "name" to whatever you type in
name = input('What is your name?')

# the print function will just say something in the terminal
# the f before the string allows the use of brackets to put variables into the print
print(f'You {name} are banished from the land of turkeys NEVER TO RETURN.')

# this creates a variable like the other one called: name
what_will_you_do = input('What do you do: fight the land of turkeys, run away and cry like a baby, stand there . ')

# basically asks if you typed 'fight the land of turkeys'
if what_will_you_do == 'fight the land of turkeys':

    # if you did type 'fight the land of turkeys'
    # it does this
    print('You were killed by your own kin... you idiot.')

    # exit() is a function that will completely stop the program
    # as shown here
    exit()

# everything VVV down is more examples of the stuff above

if what_will_you_do == 'run away and cry like a baby':
    print('You run away crying and screaming like a baby.')
    print('Everyone laughs at you.')
    exit()

if what_will_you_do == 'stand there':
    what_now = input('They peck at you wanting you to leave. what will you do now?: calmly leave, stand there . ')
    if what_now == 'calmly leave':
        print('You left the land of the turkeys never to return.')
        print('Five years later you now have a house and you are living happily. The End.')
        exit()
    if what_now == 'stand there':
        print('The turkeys take you to a cannon and stuff you into it.')
        print('You fly out of the cannon.')
        exit()






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
















