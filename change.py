def coin_change(cents):
    Q = cents // 25
    D = cents % 25 // 10
    N = cents % 25 % 10 // 5
    P = cents % 5

    print("Your change will be:")
    print("Q: ",Q)
    print("D: ",D)
    print("N: ",N)
    print("P: ",P)

print("Please enter an amount in cents less than a dollar.")
coin_change(int(input()))
