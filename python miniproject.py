class MultiplyTable():
    def table(n):
        for i in range(2,n+1): 
            print("\nMultiplication table for %d\n"%i)
            for j in range(1,11):
                print("%d x %d = %d"%(i,j,i*j))

n=int(input("Enter the value for the table :"))

print(" ~~~~~~~~~~~~~~~~~~~~~~~~")
print("|  Multiplication Table  |")
print(" ~~~~~~~~~~~~~~~~~~~~~~~~")

MultiplyTable.table(n)