from math import sqrt, acis, pi

def vzd(u, v):
    "Vzdialenosť vrcholov u, v"
    return sqrt((u.x - v.x) ** 2 + (u.y - v.y) ** 2)


def sk(u, v, w):
    "Skalárny súčin hrán uv, vw"
    return (v.x - u.x) * (w.x - u.x) + (v.y - u.y) * (w.y - u.y)


def uhol(u, v, w, form="rad"):
    if form == "rad":
        return acos(sk(u, v, w) / (vzd(u, v) * vzd(u, w)))

    if form == "deg":
        return acos(sk(u, v, w) / (vzd(u, v) * vzd(u, w))) * 180 / pi

    if form == "grad":
        return acos(sk(u, v, w) / (vzd(u, v) * vzd(u, w))) * 200 / pi

    print("Neznámy formát uhlu. Dávam výstup v radiánoch.")
    return acos(sk(u, v, w) / (vzd(u, v) * vzd(u, w)))