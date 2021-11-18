def hanoi(quant, departure, destination):
    if quant == 1:
        print(departure, destination)
    else:
        tmp = 6 - (departure + destination)
        hanoi(quant - 1, departure, tmp)
        print(departure, destination)
        hanoi(quant - 1, tmp, destination)
        
K = int(input())
print(2**K - 1)
hanoi(K, 1, 3)