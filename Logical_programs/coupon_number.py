import random
coupon_needed = int(input("Enter no. of distinct coupon needed: "))
count = 0
coupon = set()

while len(coupon) < coupon_needed:
    coupon_number = random.randint(56737,56750)
    count += 1
    coupon.add(coupon_number)

print(f"Total {count} random number needed to have all distinct numbers")
