import numpy as np

number = np.random.randint(1, 101)

count = 0
mediana = 50
step = mediana // 2
# print(number)

while True: 
    if number > mediana:
        mediana += step
        step = round(step / 2)
    elif number < mediana:
        mediana -= step
        step = round(step / 2)
    else:
        break
    count+=1
    # print(count, mediana)

print(count)
