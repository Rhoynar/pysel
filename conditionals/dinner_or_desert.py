

deserts = [
    'ice cream',
    'chocolate',
    'apple pie'
]

dinners = [
    'sandwich',
    'pasta',
    'pizza',
    'burger'
]

food_item = input('Input a food item: ')
food_item = food_item.lower()
if (food_item in dinners):
    print(food_item + ' is a DINNER!')

elif (food_item in deserts):
    print(food_item + ' is a DESSERT!')

else:
    print(food_item + ' is not listed under dinner or desserts.')
