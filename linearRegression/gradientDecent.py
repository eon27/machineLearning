import random
import math
import turtle

random.seed(1244)

X = 0
Y = 1

datasize = 25

dataset = []

for i in range(datasize):
    xVal = random.randint(0,100)
    yVal = random.randint(20,80) + math.floor(xVal/5)
    dataset.append((xVal,yVal))
print(dataset)

bias = 0
weight = 10

while True:
    loss = 0
    lossBiasUp = 0
    lossBiasDown = 0
    lossWeightUp = 0
    lossWeightDown = 0
    for j in range(datasize):
        loss += abs(dataset[j][Y] - (bias + weight * dataset[j][X]))
        lossBiasUp += abs(dataset[j][Y] - ((bias+1) + weight * dataset[j][X]))
        lossBiasDown += abs(dataset[j][Y] - ((bias-1) + weight * dataset[j][X]))
        lossWeightUp += abs(dataset[j][Y] - (bias + (weight+1) * dataset[j][X]))
        lossWeightDown += abs(dataset[j][Y] - (bias + (weight-1) * dataset[j][X]))
    loss = loss / datasize
    lossBiasUp /= datasize
    lossBiasDown /= datasize
    lossWeightUp /= datasize
    lossWeightDown /= datasize

    #print(loss)
    #print(lossBiasUp)
    #print(lossBiasDown)
    #print(lossWeightUp)
    #print(lossWeightDown)

    biasChange = 0
    weightChange = 0
    if (lossBiasUp < lossBiasDown):
        biasChange = 1
    else:
        biasChange = -1

    if (lossWeightUp < lossWeightDown):
        weightChange = 1
    else:
        weightChange = -1

    if (loss < lossWeightUp and loss < lossWeightDown):
        weightChange = 0
    if (loss < lossBiasUp and loss < lossBiasDown):
        biasChange = 0

    if (weightChange + biasChange == 0):
        break;

    bias += biasChange
    weight += weightChange

print(bias)
print(weight)

t = turtle.Turtle(visible=False)
t.speed('fastest')
t.up()

for i in range(datasize):
    t.goto(dataset[i][X]*5 - 200, dataset[i][Y]*5 - 200)
    t.dot(5, 'black')

t.goto(-200,-200)
t.down()
t.goto(-200, 300)
t.up()
t.goto(-200,-200)
t.down()
t.goto(300,-200)

turtle.mainloop()
