class vrchol:
    def __init__(self, n, x, y):
        self.cislo = n
        self.x = x
        self.y = y
        self.susedia = set()

    def pridaj_suseda(self, s, obojsmerne=True):
        self.susedia.add(s)
        s.susedia.add(self)

    def __repr__(self):
        return "Vrchol %d v (%.2f, %.2f), so susedmi %s" % (
        self.cislo, self.x, self.y, ", ".join([str(_.cislo) for _ in self.susedia]) or "∅")

    def _out(self):
        return ("[%.2f, %.2f, [" % (self.x, self.y) +
                ", ".join([str(_.cislo) for _ in self.susedia]) + "]]")

