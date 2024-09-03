class taylor:
    #static variables
    static_A = 1 
    static_B = 1 
    
    def e(self,x,n):
        if n==0:
            return 1 
        
        r = self.e(x,n-1)
        taylor.static_A *= x 
        taylor.static_B *= n 
        return r + taylor.static_A/taylor.static_B
        
        
obj = taylor()
x = int(input("Enter a number: "))
result = obj.e(x,15)
print(result)
