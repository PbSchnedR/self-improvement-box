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



class Goal:
    def __init__(self, date, items, goal_id=None):
        self.id = goal_id
        self.date = date
        self.items = items  # items est maintenant une liste de tuples (item_text, is_ticked)

    def save(self):
        """Sauvegarde le goal et ses items dans la base de données."""
        db = Database()
        try:
            if self.id:
                # Mettre à jour la date du goal
                query = "UPDATE goals SET creation_date = %s WHERE id = %s"
                db.execute_query(query, (self.date, self.id))

                # Récupérer les items actuels dans la base de données
                current_items_query = "SELECT id, item, IsTicked FROM goal_items WHERE goal_id = %s"
                current_items = db.fetch_all(current_items_query, (self.id,))

                # Convertir les résultats en un dictionnaire {item: (id, is_ticked)} pour une recherche facile
                current_items_dict = {item: (item_id, is_ticked) for (item_id, item, is_ticked) in current_items}

                # Parcourir les nouveaux items
                for new_item, is_ticked in self.items:
                    if new_item in current_items_dict:
                        # L'item existe déjà, mettre à jour son état si nécessaire
                        item_id, current_ticked = current_items_dict[new_item]
                        if current_ticked != is_ticked:
                            update_query = "UPDATE goal_items SET IsTicked = %s WHERE id = %s"
                            db.execute_query(update_query, (is_ticked, item_id))
                        del current_items_dict[new_item]
                    else:
                        # L'item est nouveau, l'insérer
                        insert_query = "INSERT INTO goal_items (goal_id, item, IsTicked) VALUES (%s, %s, %s)"
                        db.execute_query(insert_query, (self.id, new_item, is_ticked))

                # Supprimer les items qui ne sont plus dans la liste
                for old_item, (old_item_id, _) in current_items_dict.items():
                    delete_query = "DELETE FROM goal_items WHERE id = %s"
                    db.execute_query(delete_query, (old_item_id,))

            else:
                # Insérer un nouveau goal
                query = "INSERT INTO goals (creation_date) VALUES (%s)"
                db.execute_query(query, (self.date,))
                self.id = db.cursor.lastrowid

                # Insérer tous les nouveaux items
                for item, is_ticked in self.items:
                    insert_query = "INSERT INTO goal_items (goal_id, item, IsTicked) VALUES (%s, %s, %s)"
                    db.execute_query(insert_query, (self.id, item, is_ticked))

        except Exception as e:
            print(f"Erreur lors de la sauvegarde : {e}")
            raise
        finally:
            db.close()

    @staticmethod
    def get_all():
        """Récupère tous les goals et leurs items depuis la base de données."""
        db = Database()
        goals_query = "SELECT id, creation_date FROM goals"
        goals_results = db.fetch_all(goals_query)

        goals = []
        for (goal_id, date) in goals_results:
            items_query = "SELECT item, IsTicked FROM goal_items WHERE goal_id = %s"
            items_results = db.fetch_all(items_query, (goal_id,))
            items = [(item, is_ticked) for (item, is_ticked) in items_results]
            goals.append(Goal(date, items, goal_id))

        db.close()
        return goals

    def delete(self):
        """Supprime le goal et ses items de la base de données."""
        db = Database()
        query = "DELETE FROM goals WHERE id = %s"
        db.execute_query(query, (self.id,))
        db.close()