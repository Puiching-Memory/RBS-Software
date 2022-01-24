a = 'Success'

try:
    a = exec('print(1)')

except:

    a = 'Error'

finally:
    print(a)