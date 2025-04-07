uchazeci = [
    {"jmeno": "Jan Novák", "matematika": 85, "cestina": 78, "anglictina": 90},
    {"jmeno": "Petra Svobodová", "matematika": 92, "cestina": 88, "anglictina": 85},
    {"jmeno": "Karel Dvořák", "matematika": 50, "cestina": 95, "anglictina": 80},
    {"jmeno": "Eva Novotná", "matematika": 75, "cestina": 80, "anglictina": 70},


]
poradi = []

for i in uchazeci:
    body = i["matematika"] + i["cestina"] + i["anglictina"]
    if body >= 180:
        poradi.append({i['jmeno']: body})

poradi.sort(key=lambda x: list(x.values())[0], reverse=True)

for i in range(len(poradi)):
    if poradi[i] == poradi[i-1]:
        if uchazeci[i]["matematika"] > uchazeci[i-1]["matematika"]:
            poradi[i], poradi[i-1] = poradi[i-1], poradi[i]


n = 0
while n < 15:
    print(poradi[n])
    n += 1




