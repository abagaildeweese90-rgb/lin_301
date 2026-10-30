def ly_rate(words):
    total = 0
    for w in words:
        if w.endswith("ly"):
            total += 1
    return total / len(words) * 1000