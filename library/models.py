from django.db import models
from django.db import transaction

class Author(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    birth_date = models.DateField()
    
    def getId(self):  
        return f"auth-{self.id}" 

    def getAuthor(self): 
        return {
            'id': self.getId(),
            'name': self.name,
            'nationality': self.nationality,
            'birth_date': self.birth_date
        }

    @classmethod
    def insertAuthors(cls, authors_list):
        try:
            with transaction.atomic():
                for author_data in authors_list:
                    cls.objects.create(
                        name=author_data.get("name"),
                        nationality=author_data.get("nationality"),
                        birth_date=author_data.get("birth_date")
                    )
                return True
        except Exception as e:
            print(f"Error: {str(e)}")
            return False

    @classmethod
    def updateAuthors(cls, authors_list):
        try:
            with transaction.atomic():
                for author_data in authors_list:
                    author_id = author_data.get("id")
                    if not author_id or not author_id.startswith("auth-"):
                        raise ValueError("id author not found or incorrect")
                    author_id = author_id[5:]
                    author = cls.objects.get(id=author_id)
                    author.name = author_data.get("name", author.name)
                    author.nationality = author_data.get("nationality", author.nationality)
                    author.birth_date = author_data.get("birth_date", author.birth_date)
                    author.save()
                return True
        except cls.DoesNotExist:
            return False
        except ValueError as ve:
            return False
        except Exception as e:
            return False

    @classmethod
    def deleteAuthors(cls, authors_list):
        try:
            with transaction.atomic():
                for author_id in authors_list:
                    if not author_id.startswith("auth-"):
                        raise ValueError("id not found")
                    numeric_id = author_id[5:]
                    author = cls.objects.get(id=numeric_id)
                    author.delete()
                return True
        except cls.DoesNotExist:
            return False
        except ValueError as ve:
            return False
        except Exception as e:
            return False

    @classmethod
    def selectAuthors(cls, id=None):
        try:
            if id:
                if not id.startswith("auth-"):
                    raise ValueError("error")
                numeric_id = id[5:]
                author = cls.objects.get(id=numeric_id)
                return [author.getAuthor()] 
            else:
                authors = cls.objects.all()
                return [author.getAuthor() for author in authors] 
        except cls.DoesNotExist:
            return []
        except ValueError as ve:
            return []
        except Exception as e:
            return []
        
    @classmethod
    def selectAuthorsByNationality(cls, nationality):
        try:
            authors = cls.objects.filter(nationality=nationality)
            data = [author.getAuthor() for author in authors]
            return data
        except Exception as e:
            return []
     
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    genre = models.CharField(max_length=50 ,default='General')
    published_date = models.DateField(null=True)

    def getId(self):
        return f"book-{self.id}"
    
    def getBook(self):
        return {
            'id': self.getId(),
            'title': self.title,
            'author': self.author.getAuthor(),
            'genre': self.genre,
            'published_date': self.published_date,
        }

    @classmethod
    def insertBooks(cls, books_list):
        try:
            with transaction.atomic():  
                for book_data in books_list:
                    cls.objects.create(
                        title=book_data.get("title"),
                        author=book_data.get("author"),  
                        genre=book_data.get("genre"),
                        published_date=book_data.get("published_date")
                    )
                return True  
        except Exception as e:
            print(e)
            return False

    @classmethod
    def updateBooks(cls, books_list):
        try:
            with transaction.atomic():
                for book_data in books_list:
                    book_id = book_data.get("id")
                    if not book_id or not book_id.startswith("book-"):
                        raise ValueError("id book not found or incorrect")
                    book_id = book_id[5:]
                    book = cls.objects.get(id=book_id)
                    book.title = book_data.get("title", book.title)
                    book.author = book_data.get("author", book.author)
                    book.genre = book_data.get("genre", book.genre)
                    book.published_date = book_data.get("published_date", book.published_date)
                    book.save()
                return True 
        except cls.DoesNotExist:
            return False
        except ValueError as ve:
            return False
        except Exception as e:
            return False

    @classmethod
    def deleteBooks(cls, books_list):
        try:
            with transaction.atomic(): 
                for book_id in books_list:
                    if not book_id.startswith("book-"):
                        raise ValueError("id not found")
                    numeric_id = book_id[5:]
                    book = cls.objects.get(id=numeric_id)
                    book.delete()
                return True 
        except cls.DoesNotExist:
            return False
        except ValueError as ve:
            return False
        except Exception as e:
            return False

    @classmethod
    def selectBooks(cls, id=None):
        try:
            if id:
                if not id.startswith("book-"):
                    raise ValueError("error")
                numeric_id = id[5:]
                book = cls.objects.get(id=numeric_id)
                print(books)
                return [book.getBook()]
            else:
                books = cls.objects.all()
                print(books)
                return [book.getBook() for book in books]
        except cls.DoesNotExist:
            return ['errr1']
        except ValueError as ve:
            return ['errre4']
        except Exception as e:
            return ['uuu7']
    
    @classmethod
    def selectBooksByGenre(cls, genre):
        try:
            books = cls.objects.filter(genre=genre)
            data = [book.getBook() for book in books]
            return data
        except Exception as e:
            return []

    def __str__(self):
        return self.title
