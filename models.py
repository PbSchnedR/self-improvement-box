class Idea:
    def __init__(self, content):
        self.content = content

Ideas = [
            Idea("Aller à la montagne"),
            Idea("Passer le balai"),
            Idea("Cuisiner")
        ]

class Goal:
    def __init__(self, date, items):
        self.date = date
        self.items = items

Goals = [
    Goal("29-09-2006" , ["se lever à 7h", "bien manger"]),
    Goal("29-09-2006" , ["se lever à 9h", "bien dormir"]),
    Goal("29-09-2006" , ["se lever à 17h", "bien fumer"])
]