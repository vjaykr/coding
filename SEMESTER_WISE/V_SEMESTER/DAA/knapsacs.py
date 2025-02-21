objects = [1,2,3,4,5,6,7]
profits = [10,5,15,7,6,18,3]
weights = [2,3,5,7,1,4,1]
n = 7
knapsackweightmaxallowed = 15
PPU = []
for i in range (len(profits)):
    PPU.append((profits[i]/weights[i], weights[i]))
    
PPU.sort(reverse = True)
print(PPU)
maxprofit = 0
for crr in PPU:
    if knapsackweightmaxallowed == 0:
        break
    CP, CW = crr[0], crr[1]
    print(CW,CP)

    if CW < knapsackweightmaxallowed:
        knapsackweightmaxallowed -= CW
        maxprofit += CP * CW
        
    else:
        maxprofit += knapsackweightmaxallowed * CP
        knapsackweightmaxallowed = 0
    print(knapsackweightmaxallowed,"remaining weight")
print(maxprofit)        
      