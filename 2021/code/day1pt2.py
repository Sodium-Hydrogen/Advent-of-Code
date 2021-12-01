from day1pt1 import depths, cnt

if __name__ == "__main__":
    for n in range(3, len(depths)):
        if sum(depths[n-2:n+1]) > sum(depths[n-3:n]):
            cnt += 1
    print(f"Total moving average increases: {cnt}")
