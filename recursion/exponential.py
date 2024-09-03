'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
def power(m,n):
    if n==0:
        return 1 
    else:
        return m*pow(m,n-1)
        
if __name__ == "__main__":
    m = int(input("Enter a number: "))
    result = power(m, 3)
    print(result)