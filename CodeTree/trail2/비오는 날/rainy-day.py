n = int(input())
date = []
day = []
weather = []
rain = []

class Rain:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)
    rain.append(Rain(d, dy, w))

for r in rain:
    if r.weather == 'Rain':
        result = r
        break

for r in rain:
    if r.weather == 'Rain' and r.date < result.date:
        result = r

print(result.date, result.day, result.weather)