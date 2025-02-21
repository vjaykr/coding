def main():
    saving = int(input())
    n = int(input())
    currentvalue = []
    for _ in range(n):
        currentvalue.append(int(input()))
    a = int(input())
    futurevalue = []
    for _ in range(a):
        futurevalue.append(int(input()))
    dp = [0] * (saving + 1)
    for i in range(saving + 1):
        for j in range(saving, currentvalue[i] - 1, -1):
            dp[j] = max(dp[j], dp[j - currentvalue[i]] + futurevalue[i] - currentvalue[i])
    print(dp[saving])

if __name__ == "__main__":
    main()