class life:
    map = []
    def __init__(self,n,p):
        self.row = int(n)
        self.center = int(n/2-0.5)
        for i in range(1,n+1):
            self.map.append(['*']*n)
        if(p==1):
            self.map[self.center-1][self.center]=0
            self.map[self.center-1][self.center-1]=0
            self.map[self.center-1][self.center+1]=0
            self.map[self.center][self.center-1]=0
            self.map[self.center+1][self.center]=0
        else:
            return None
    def display(self):
        for i in range(0,self.row):
            for j in range(0,self.row):
                print(self.map[i][j],end='')
            print()

x = life(5,1)
x.display()