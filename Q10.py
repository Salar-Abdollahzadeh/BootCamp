num = int(input("Enter the number: "))
reversenum = 0


def reverse(num):
    '''
    global variable
     یادت که نرفته؟؟؟
     اکه آره ی سفر برو

   '''
    global reversenum

    if (num > 0):
        Reminder = num % 10
        reversenum = (reversenum * 10) + Reminder
        reverse(num // 10)

        '''
        palindrome
        میدونی به چی میگن؟

        '''

        if (num == reversenum):
            print('ops there is palindrome')
        else:
            return reversenum


reversenum = reverse(num)
print(f'reverse of Enter number is {reversenum}')
