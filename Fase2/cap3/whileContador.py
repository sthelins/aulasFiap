
n = int(input("De qual número você quer a tabuada? "))
i = 1
conta = 0

while i <= 10:
    conta = i * n
    print(f"{i} x {n} = {conta}")
    i = i + 1