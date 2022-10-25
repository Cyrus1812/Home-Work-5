# Задача 4*. Создайте игру в крестики-нолики.
print("Приветствую вас в игре крестики нолики!")
name1 = input("Введите имя первого игрока ")
name2 = input("Введите имя второго игрока ")
print("Ваше поле")
map =[[0,1,2,3],[1,0,0,0],[2,0,0,0],[3,0,0,0]]
for i in range(0,len(map)):
    print(map[i])
x="x"
y ="y"
player1 = "Ходит "+ name1 
player2 = "Ходит "+ name2 
result1 = "Выиграл 1 игрок"
result2 = "Выиграл 2 игрок"
for i in range(0,5):

    print(player1)
    line =int(input("Выберите линию: "))
    column = int(input("Выберите столбец: "))
    fok = map[line]
    fok[column] = x
    map[line] = fok
    for i in range(0,len(map)):
        print(map[i])

    if  map[1][1] == map[1][2] == map[1][3]==x or map[2][1] == map[2][2] == map[2][3]==x or map[3][1] == map[3][2] == map[3][3]==x or map[1][1] == map[2][1] == map[3][1]==x or map[1][2] == map[2][2] == map[3][2]==x or map[1][3] == map[2][3] == map[3][3]==x or map[1][1] == map[2][2] == map[3][3]==x or map[1][3] == map[2][2] == map[3][1] == x:
        print(result1)
        break
    if map[1][1] !=0 and map[1][2] !=0 and map[1][3]!=0 and map[2][1]!=0 and map[2][2]!=0 and map[2][3]!=0 and map[3][1]!=0 and map[3][2]!=0 and map[3][3]!=0:
        print("Ничья")
        break

    print(player2)
    line =int(input("Выберите линию: "))
    column = int(input("Выберите столбец: "))
    fok = map[line]
    fok[column] = y
    map[line] = fok
    for i in range(0,len(map)):
        print(map[i])
    if  map[1][1] == map[1][2] == map[1][3]==y or map[2][1] == map[2][2] == map[2][3]==y or map[3][1] == map[3][2] == map[3][3]==y  or map[1][1] == map[2][1] == map[3][1]==y  or map[1][2] == map[2][2] == map[3][2]==y  or map[1][3] == map[2][3] == map[3][3]==y  or map[1][1] == map[2][2] == map[3][3]==y  or map[1][3] == map[2][2] == map[3][1] == y:
        print(result2)
        break
   
    
    
    
