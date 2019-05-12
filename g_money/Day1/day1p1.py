# ============================
# === Day 1 P1 - Version 1 ===
# ============================

fname = open('day1p1.txt')
total = 0

for i in fname:
    total = total + int(i)
print(total)


# ============================
# === Day 1 P1 - Version 2 ===
# ============================

fname = open('day1p1.txt')
lst = list()

for i in fname:
    lst.append(int(i))
print(sum(lst))
