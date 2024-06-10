from models.connection2 import get_db_connection

class Article:
    def __init__(self, id, title, content, author_id, magazine_id):
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id
        self._create_in_db()

    def _create_in_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO articles (id, title, content, author_id, magazine_id) VALUES (?, ?, ?, ?, ?)',
                       (self.id, self.title, self.content, self.author_id, self.magazine_id))
        conn.commit()
        conn.close()

    def __repr__(self):
        return f'<Article {self.title}>'
