print('Reboot the computer and try to connect.')
ans = input('Did that fix the problem?')
if ans == 'no':
    print('Reboot the router and try to connect.')
    ans = input('Did that fix the problem?')
    if ans == 'no':
        print('Make sure the cables betwwen the router & modem are plugged in firmly.')
        ans = input('Did that fix the problem?')
        if ans == 'no':
            print('Move the router to a new locaiton and try to connect.')
            ans = input('Did that fix the problem?')
            if ans == 'no':
                print('Get a new router')
else:
    print('All done.')
