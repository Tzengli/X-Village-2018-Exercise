class life:
    map = []
    def set_map(self,n):
        self.row = int(n)
        self.center = int(self.row/2-0.5)
        for i in range(1,self.row+1):
            self.map.append(['*']*self.row)
    
    def display(self):
        for i in range(0,self.row):
            for j in range(0,self.row):
                print(self.map[i][j],end='')
            print("")
    def set_pattern(self,n):
        if (n==1):
            self.map[self.center-1][self.center]=0
            self.map[self.center-1][self.center-1]=0
            self.map[self.center-1][self.center+1]=0
            self.map[self.center][self.center-1]=0
            self.map[self.center+1][self.center]=0
        else :
            return 0
        
x=life()
x.set_map(5)
x.display()
print("")
x.set_pattern(1)
x.display()


        



