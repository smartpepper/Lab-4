things = [   ['r',3, 25, 0],
        ['p',2, 15, 0],
        ['a',2, 15, 0],
        ['m',2, 20, 0],
        ['i',1, 5, 0],
        ['k',1, 15, 0],
        ['x',3, 20, 0],
        ['t',1, 25, 0],
        ['f',1, 15, 0],
        ['d',1, 10, 0],
        ['s',2, 20, 0],
        ['c',2, 20, 0]
]
for i in things:
    i[3]=i[2]/i[1]
things = sorted(things, key=lambda x: (x[3], x[1]))
things.reverse()
my_place=9 # место в рюкзаке
place_7=7 # место в рюкзаке в доп задании
place=0
cost=10 # очки выживания
problem=0
bag =''
for i in things:
    if place<my_place:
        place+=i[1]
        cost+=i[2]
        last_place=i[1] 
        last_cost=i[2] 
        bag = bag+i[0]*int(i[1])
        thing =i[0]*int(i[1])
    else:
        if place==my_place:
            cost-=i[2]
        else:
            print("не фартануло")
            # мне повезло, нет проблем)))
for i in range(0,9,3):
    print(bag[i],bag[i+1],bag[i+2])
print('мои итоговые очки выживания:',cost)

place=0
cost=10 # очки выживания
problem=0
bag =''
for i in things:
    if place<place_7:
        place+=i[1]
        cost+=i[2]
        last_place=i[1] 
        last_cost=i[2] 
        bag = bag+i[0]*int(i[1])
        thing =i[0]*int(i[1])
    else:
        if place==place_7:
            cost-=i[2]
        else:
            print("не фартануло")
            # мне повезло, нет проблем))
print("---------------------------------")
for i in bag:
    print("["+i+"]")
print('итоговые очки выживания для 7 ячеек:',cost)
if cost<=0:
    print("Решение отсутствует для 7 ячеек")
