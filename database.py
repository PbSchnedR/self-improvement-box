import mysql.connector

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="m$0SPl666*hi4nte",
            database="selfi_box"
        )
        self.cursor = self.connection.cursor(buffered=True)  # Curseur bufferisé

    def execute_query(self, query, params=None):
        """Exécute une requête SQL."""
        self.cursor.execute(query, params or ())
        self.connection.commit()

    def fetch_all(self, query, params=None):
        """Récupère tous les résultats d'une requête."""
        self.cursor.execute(query, params or ())
        return self.cursor.fetchall()

    def close(self):
        if self.cursor:
            try:
                # Lire tous les résultats non lus
                self.cursor.fetchall()
            except mysql.connector.errors.InterfaceError:
                # Pas de résultats à lire
                pass
            finally:
                self.cursor.close()
        if self.connection:
            self.connection.close()