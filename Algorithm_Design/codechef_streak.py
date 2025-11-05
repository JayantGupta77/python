def longest_streak(arr):
    maxi = curr = 0
    for num in arr:
        if num > 0:
            curr += 1
            maxi = max(maxi, curr)
        else:
            curr = 0
    return maxi

n = int(input())
om = list(map(int, input().split()))
addy = list(map(int, input().split()))

om_streak = longest_streak(om)
addy_streak = longest_streak(addy)

if om_streak > addy_streak:
    print("Om")
elif om_streak < addy_streak:
    print("Addy")
else:
    print("Draw")
