import math,time

print('\nRight angle triangle program')
print('\nLoading....')
time.sleep(2)

try:
    hypo  =  float(input('\tHypotenuse:'))
    base  =  float(input('\tBase:'))
    alt  =  float(input('\tAltitude:'))

    total = math.sqrt(base**2 + alt**2)
    print('\n\tthe sum of base and altitude squares:' + str(total))
    print('\tthe square of hypotenuse:' + str(hypo))
    if total == hypo:
        print('\n\tIt is a right angled triangle')
    else:
        print('\n\t It is not a right angled triangle')
except:
    print('\n\tError occured! Please check inputs')
    
    print('created sidharth72')
