# time complexity :the rate of increse in time with respect to increse in the inputfor
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j)
        # in above code tc is o(n^2) because we have two nested loops each running n times

for i in range(1,n+1):
    for j in range(i,n+1):
        print(i,j)
        #in naturally it is n(n+1)/2 but in big o notation we ignore the constant and lower order term so it is o(n^2)
