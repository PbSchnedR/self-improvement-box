from database import Database

class Idea:
    def __init__(self, content, idea_id=None):
        self.id = idea_id
        self.content = content

    def save(self):
        """Sauvegarde l'idée dans la base de données."""
        db = Database()
        if self.id:
            # Mettre à jour une idée existante
            query = "UPDATE ideas SET content = %s WHERE id = %s"
            db.execute_query(query, (self.content, self.id))
        else:
            # Insérer une nouvelle idée
            query = "INSERT INTO ideas (content) VALUES (%s)"
            db.execute_query(query, (self.content,))
            self.id = db.cursor.lastrowid  # Récupérer l'ID généré
        db.close()

    @staticmethod
    def get_all():
        """Récupère toutes les idées depuis la base de données."""
        db = Database()
        query = "SELECT id, content FROM ideas"
        results = db.fetch_all(query)
        db.close()
        return [Idea(content, idea_id) for (idea_id, content) in results]

    def delete(self):
        """Supprime l'idée de la base de données."""
        db = Database()
        query = "DELETE FROM ideas WHERE id = %s"
        db.execute_query(query, (self.id,))
        db.close()

class Ideas:
    @staticmethod
    def get_all():
        return Idea.get_all()

    @staticmethod
    def add(idea):
        idea.save()

    @staticmethod
    def remove(idea):
        idea.delete()

class Goal:
    def __init__(self, date, items):
        self.date = date
        self.items = items

Goals = [
    Goal("29-09-2006" , ["se lever à 7h", "bien manger"]),
    Goal("29-09-2006" , ["se lever à 9h", "bien dormir"]),
    Goal("29-09-2006" , ["se lever à 17h", "bien fumer"])
]