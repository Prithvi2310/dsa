def pattern(n):
    current_number = 1
    for i in range(1,n+1):

        if i % 2 != 0:
            for j in range(4):
                print(current_number, end=" ")
            print(current_number+1, end=" ")
            print("\n")
        elif i % 2 == 0:
            print(current_number+1, end=" ")
            for j in range(4):
                print(current_number, end=" ")
            print("\n")
                
        current_number = current_number + 1
                    
                    
n = int(input("Enter a number: "))
pattern(n)