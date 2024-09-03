'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
class taylor_horner_rule:
    static_sum = 1 
    
    def e(self,x,n):
        if n==0:
            return taylor_horner_rule.static_sum
        taylor_horner_rule.static_sum = 1 + x/n*taylor_horner_rule.static_sum
        return self.e(x,n-1)

if __name__ == "__main__":
    n=4
    obj = taylor_horner_rule()
    x = int(input("Enter a number: ")) 
    result = obj.e(x,n)
    print(result)
