import math

cycle = ['SPD', 'AV']
for i in range(1, 11):
    cycle.append(f'c{i}')
# print(cycle)


matrix = []
matrix.append(cycle)

cycle_av = [0,150,250,350,450,550,650,750,850,950,1050]

for spd in range(100, 195):
    av = math.ceil(10000/spd)
    if(str(av) == matrix[-1][1]):
        continue
    row = [str(spd), str(av), '0']
    running_av = 0
    cav = 1
    switch = 'off'  
    while(running_av + av < 1050):
        running_av += av
        if(running_av <= cycle_av[cav]):
            # if(len(row[-1]) > 0):
                # row[-1] += ','
            # row[-1] += str(running_av)
            row[-1] = str(int(row[-1]) + 1)
        else:
            cav += 1
            # row.append(str(running_av))
            row.append(str(1))
    row.append(0)
    for i in range(2, 12):
        row[-1] += int(row[i])
    matrix.append(row)




for row in matrix:
    for i in row:
        print(f'{i}  ', end='')
    print('\n')
