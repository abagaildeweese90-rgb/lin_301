languages = ["Hittite", "Sanskrit", "Latin", "Gothic", "Tocharian"]
dates = [-1650, -1200, -700, 350, 600]

latin_index = languages.index("Latin")
print(dates[latin_index])   # -700

gothic_index = languages.index("Gothic")
print(dates[gothic_index])  # 350

attested = {
    "Hittite": -1650,
    "Sanskrit": -1200,
    "Latin": -700,
    "Gothic": 350,
    "Tocharian": 600
}
print(attested["Latin"])   # -700

print("Old Irish" in attested)   # False


attested["Old Irish"] = 700
print(attested)

del attested["Tocharian"]
print(attested)