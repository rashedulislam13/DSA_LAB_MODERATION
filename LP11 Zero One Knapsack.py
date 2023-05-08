11# Knapsack using dynamic programming
def zero_one_knapsack(Capacity, weight, profits, n):
    Array = [[0 for x in range(Capacity + 1)] for x in range(n + 1)]
    # Table in bottom up manner
    for i in range(n + 1):
        for w in range(Capacity + 1):
            if i == 0 or w == 0:
                Array[i][w] = 0
            elif weight[i - 1] <= w:
                Array[i][w] = max(profits[i - 1] + Array[i - 1][w - weight[i - 1]], Array[i - 1][w])
            else:
                Array[i][w] = Array[i - 1][w]
    return Array[n][Capacity]


# Matrix for create another matrix.
def knapsack_Matrix(Capacity, weight, profits, n):
    Matrix = [[0 for x in range(Capacity + 1)] for x in range(n + 1)]
    # Table in bottom up manner
    for i in range(n + 1):
        for w in range(Capacity + 1):
            if i == 0 or w == 0:
                Matrix[i][w] = 0
            elif weight[i - 1] <= w:
                Matrix[i][w] = max(profits[i - 1] + Matrix[i - 1][w - weight[i - 1]], Matrix[i - 1][w])
            else:
                Matrix[i][w] = Matrix[i - 1][w]
    print("The Matrix for zero one knapsack : ")
    for i in range(len(Matrix)):
        for j in range(len(Matrix[i])):
            print(Matrix[i][j], end=' ')
        print()


# fucntion close

profits = [int(item) for item in input("Enter the Profit value : ").split()]
weight = [int(item) for item in input("Enter the weight value : ").split()]
C = int(input("Enter the Capacity : "))
n = int(input("Enter the number of item : "))
knapsack_Matrix(C, weight, profits, n)
print("Maximum profit from this matrix using zero one knapsack method : ")
print(zero_one_knapsack(C, weight, profits, n))
