minutes = int(input('Enter the number of minutes: '))

hours = int(minutes/60)
mins = minutes % 60

print(str(minutes) + ' is same as: ' + str(hours) + ' hrs and ' + str(mins) + ' mins')
