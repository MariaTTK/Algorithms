denomination=[1,2,3]
amount = 4

comb=[]
def total_amount(coin):
    total = []
    while sum(total, coin) <= amount:
        total.append(coin)
        if sum(total) < amount:
            comb.append(total)
        print("Total: ", total)
        print("Combination: ", comb)

for d in denomination:
    total_amount(d)


