string = input()  

#if the string length is odd, do not check
if len(string) % 2 == 1:
    print('false')
else:
    while 1:
        length_str = len(string)

        #getting rid of closing brackets
        string = string.replace('{}', '').replace('[]', '').replace('()', '')

        #if we got rid of all pairs of brackets the string was correct
        if len(string) == 0:
            print('true')
            break

        #if the string length has not changed after deleting pairs, then an incorrect pair has been found
        elif len(string) == length_str:
            print('false')
            break