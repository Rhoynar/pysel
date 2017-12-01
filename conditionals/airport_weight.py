# Luggage Weight Table.
#   Weight       Surcharge
#   0-20 lb  ==> $30
#   20-30 lb ==> $40
#   30-40 lb ==> $50
#   40-50 lb ==> $60
#   50+ lb   ==> Not allowed.

weight = int(input('Enter Luggage Weight: '))

if weight < 20:
  print('Weight: ' + 'No surcharge')
elif 20 <= weight < 30:
  print('Weight:', weight, 'Surcharge: $40')
elif 30 <= weight < 40:
  print('Weight:', weight, 'Surcharge: $50')
elif 40 <= weight < 50:
  print('Weight:', weight, 'Surcharge: $60')
else:
  print('Weight:', weight, 'Luggage not allowed!')