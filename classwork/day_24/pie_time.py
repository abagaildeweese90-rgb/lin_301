import pandas as pd

root    = ["*bʰer-", "*ĝenh₁-", "*ped-", "*doh₃-"]
meaning = ["to carry", "to beget", "foot", "to give"]
latin   = ["ferō", "gignō", "pēs", "dō"]
greek   = ["pʰérō", "gígnomai", "poús", "dídōmi"]
english = ["bear", "kin", "foot", "donate"]

pie_time = []

for r, m, l, g, e in zip(root, meaning, latin, greek, english):
    pie_time.append({
        "root": r,
        "meaning": m,
        "latin": l,
        "greek": g,
        "english": e
    })

pie_time = pd.DataFrame(pie_time)
print(pie_time)

pie_time.to_csv("pie_time.csv", index=False, encoding="utf-8-sig")

check = pd.read_csv("pie_time.csv")
print(check)
