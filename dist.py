# distance calculator program
from numerizer import numerize

print('\nTime calculater constant(300000 km/s)')
try:
    from_ = input('\nfrom where:')
    to = input('To:')
    numerized_distance = numerize(input('Enter distance in km:'))
    dist = int(numerized_distance)
    
    # storing operations in variables
    
    time_taken = dist/300000
    in_min = time_taken/60
    in_hr = in_min/60
    in_day = in_hr/24
    in_year = in_day/365
    
    
    
    if in_min >= 60:
        print('\nTo reach:' + str(in_hr) + ' ' + 'hours at lightspeed to reach from ' + ' ' + from_ +""+ 'to' +" "+ to )
    if in_hr >= 24:
        print('\nTo reach:' + str(in_day) + ' ' + 'days at lightspeed to reach from' + ' ' + from_ +""+'to' +" "+ to)
    if in_day >= 365:
        print('\n To reach:' + str(in_year) + ' ' + 'light years to reach from' + ' ' + from_ + " " + 'to' + " " + to)
    else: 
        print('\n To reach:' + str(in_min) + ' ' 'minutes to reach from' + " " + from_ + " " + 'to' +" "+ to)
    
except:
    print('Cant execute program something went wrong!!')
    