plansza=[]
done=False
moves=[[1,-2],[2,-1],[-2,-1],[-1,2],[-1,-2],[1,2],[-2,1],[2,1]]

def wyn(T):
    for i in T:
        print(i)
        
def skoczek(x=0,y=0,licz=2):
    global plansza, done, moves
    for move in moves:
        if x+move[0]>-1 and x+move[0]<len(plansza) and y+move[1]>-1 and y+move[1]<len(plansza) and plansza[y+move[1]][x+move[0]]==0:
            plansza[y+move[1]][x+move[0]]=licz
            skoczek(x+move[0],y+move[1],licz+1)
            if done:
                return
    
    if licz==((len(plansza))**2)+1:
        done=True
        wyn(plansza)
        return
    
    plansza[y][x]=0
    return
    
def main():
    global plansza
    n=int(input('Podaj bok planszy: '))
    plansza=[[0]*n for _ in range(n)]
    plansza[0][0]=1
    skoczek()
    print("KONIEC")
    input()

if __name__=='__main__':
    main()

        
    
