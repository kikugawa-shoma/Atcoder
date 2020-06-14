S = input()

week = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]

for i, day in enumerate(week):
    if day == S:
        day_num = i
        break

print(7-i)

