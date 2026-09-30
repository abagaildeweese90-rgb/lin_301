try:
    with open("mystery_novel.txt", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("Couldn't find that file — check the filename and location.")