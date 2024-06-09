
from database.connection import get_db_connection

class Magazine:
    def _init_(self, name, category):
        self._name = name
        self._category = category
        self._id = self.create_magazine()

    def create_magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO magazines (name, category) VALUES (?, ?)', (self._name, self._category))
        conn.commit()
        magazine_id = cursor.lastrowid
        conn.close()
        return magazine_id

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('UPDATE magazines SET name = ? WHERE id = ?', (self._name, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Name must be a string between 2 and 16 characters")

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('UPDATE magazines SET category = ? WHERE id = ?', (self._category, self._id))
            conn.commit()
            conn.close()
        else:
            raise ValueError("Category must be a non-empty string")

    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM articles WHERE magazine_id = ?
        ''', (self._id,))
        articles = cursor.fetchall()
        conn.close()
        return [article(article["id"], article["title"], article["content"], article["author_id"], article["magazine_id"]) for article in articles]

    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON articles.author_id = authors.id
            WHERE articles.magazine_id = ?
        ''', (self._id,))
        authors = cursor.fetchall()
        conn.close()
        return [author(author["id"], author["name"]) for author in authors]

    def _repr_(self):
        return f'<Magazine {self.name}>'