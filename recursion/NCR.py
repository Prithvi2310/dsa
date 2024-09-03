def fact(n):
    if n==1:
        return 1 
        
    return fact(n-1)*n 

def ncr(n,r):
    num = fact(n)
    den = fact(r)*fact(n-r)
    return num/den
    
def NCR(n,r):
    if n==r or r==0:
        return 1 
    
    return NCR(n-1,r-1) + NCR(n-1,r)
    
if __name__ == "__main__":
    n,r = map(int,input("Enter values for n and r: ").split(" "))
    res = NCR(n,r)
    print(res)