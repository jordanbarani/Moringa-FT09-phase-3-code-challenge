
from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Create an author
    author = Author(author_name)

    # Create a magazine
    magazine = Magazine(magazine_name, magazine_category)

    # Create an article
    article = Article(author, magazine, article_title, article_content)

    # Display results
    print("\nAuthors:")
    print(author)

    print("\nMagazines:")
    print(magazine)

    print("\nArticles:")
    print(article)

    print("\nAuthor's Articles:")
    for article in author.articles():
        print(article)

    print("\nAuthor's Magazines:")
    for mag in author.magazines():
        print(mag)

    print("\nMagazine's Articles:")
    for article in magazine.articles():
        print(article)

    print("\nMagazine's Contributors:")
    for contributor in magazine.contributors():
        print(contributor)

if __name__ == "_main_":
    main()