#Реализуйте алгоритм перемешивания списка.

import random

list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_shuffled = []
for i in range(0, len(list)):
    j = random.randrange(0, len(list))
    list_shuffled.append(list[j])
    list.remove(list[j])
print(list_shuffled)