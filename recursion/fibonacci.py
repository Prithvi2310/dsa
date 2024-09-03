def fib(n):
    if n<=1:
        return n 
        
    t0 = 0 
    t1 = 1 
    s = 0 
    for i in range(1,n):
        s = t0 + t1 
        t0 = t1 
        t1 = s 
        
    return s 
    
def rfib(n):
    if n<=1:
        return n 
    
    return rfib(n-2) + rfib(n-1)
    
#recusion with memoization
def mfib(n):
    if n<=1:
        mem_buff[n] = n 
        return n 
    else:
        if mem_buff[n-2] == -1:
            mem_buff[n-2] = mfib(n-2)
        if mem_buff[n-1] == -1:
            mem_buff[n-1] = mfib(n-1)
        mem_buff[n] = mem_buff[n-2] + mem_buff[n-1]
        return mem_buff[n]
    
if __name__ == "__main__":
    n = int(input("Enter a number: "))
    mem_buff = [-1]*(n+1)
    result = mfib(n)
    print(result)
    print(mem_buff)