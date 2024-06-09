
from database.connection import get_db_connection

class Author:
    def _init_(self, name):
        self._name = name
        self._id = self.create_author()

    def create_author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO authors (name) VALUES (?)', (self._name,))
        conn.commit()
        author_id = cursor.lastrowid
        conn.close()
        return author_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE author_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        ''', (self._id,))
        magazines = cursor.fetchall()
        conn.close()
        return [magazine(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]

    def _repr_(self):
        return f'<Author {self.name}>'