from models.connection2 import get_db_connection

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.id = None  # Initialize id as None

        self._create_in_db()

    def _create_in_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self.name, self.category))
        # Retrieve the id of the newly inserted row
        self.id = cursor.lastrowid
        conn.commit()
        conn.close()

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM articles WHERE magazine_id = ?', (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors

    def __repr__(self):
        return f'<Magazine {self.name}>'
