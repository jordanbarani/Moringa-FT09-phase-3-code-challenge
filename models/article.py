
from database.connection import get_db_connection

class Article:
    def _init_(self, author, magazine, title, content):
        self._author = author
        self._magazine = magazine
        self._title = title
        self._content = content
        self._id = self.create_article()

    def create_article(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, author_id, magazine_id) 
            VALUES (?, ?, ?, ?)
        ''', (self._title, self._content, self._author.id, self._magazine.id))
        conn.commit()
        article_id = cursor.lastrowid
        conn.close()
        return article_id

    @property
    def id(self):
        return self._id

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

    def _repr_(self):
        return f'<Article {self.title}>'