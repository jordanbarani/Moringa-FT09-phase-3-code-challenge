import unittest
from models.author import Author
from models.article import Article
from models.magazine import Magazine
from models.connection2 import get_db_connection

def setup_database():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Drop tables if they exist to start with a clean state
    cursor.execute('DROP TABLE IF EXISTS authors')
    cursor.execute('DROP TABLE IF EXISTS magazines')
    cursor.execute('DROP TABLE IF EXISTS articles')
    # Create tables
    cursor.execute('CREATE TABLE authors (id INTEGER PRIMARY KEY, name TEXT)')
    cursor.execute('CREATE TABLE magazines (id INTEGER PRIMARY KEY, name TEXT, category TEXT)')
    cursor.execute('CREATE TABLE articles (id INTEGER PRIMARY KEY, title TEXT, content TEXT, author_id INTEGER, magazine_id INTEGER)')
    conn.commit()
    conn.close()

class TestModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        setup_database()

    def test_author_creation(self):
        author = Author(1, "John Doe")
        self.assertEqual(author.name, "John Doe")

    def test_article_creation(self):
        author = Author(2, "Jane Doe")
        magazine = Magazine("Tech Weekly", "Technology")  # Removed the first argument
        article = Article(1, "Test Title", "Test Content", author.id, magazine.id)
        self.assertEqual(article.title, "Test Title")

    def test_magazine_creation(self):
        magazine = Magazine("Tech Weekly", "Technology")  # Removed the first argument
        self.assertEqual(magazine.name, "Tech Weekly")
        self.assertEqual(magazine.category, "Technology")

if __name__ == "__main__":
    unittest.main()
