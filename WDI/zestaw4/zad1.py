def print_tab(tab):
    for line in tab:
        print(line)

n=int(input("Podaj bok kwadratu: "))
tab=[[0]*n for _ in range(n)]
x,y=0,0
i = 1
maxi = n**2
while i <= maxi:
    while x < n-1 and tab[y][x+1] == 0:
        tab[y][x] = i
        x += 1
        i += 1

    while y < n-1 and tab[y+1][x] == 0:
        tab[y][x] = i
        y += 1
        i += 1

    while x > 0 and tab[y][x-1] == 0:
        tab[y][x] = i
        x -= 1
        i += 1

    while y > 0 and tab[y-1][x] == 0:
        tab[y][x] = i
        y -= 1
        i += 1

    if i == maxi:
        tab[y][x] = i
        i += 1
print_tab(tab)

