# Input temperature and print if its hot or cold

temp = int(input('Enter current temperature: '))

if temp < 50:
    print('It\'s COLD!')
elif temp > 80:
    print('It\'s HOT!')
else:
    print('It\'s NICE!')
