def np(t):
    for wiersz in t:
        for liczba in wiersz:
            s=str(liczba)
            e=0
            for cyfra in s:
                if int(cyfra)%2==0:
                    e=1
                    break
            if e==0:
                break
        if e==1:
            return True
    return False
