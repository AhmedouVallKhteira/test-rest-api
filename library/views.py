from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Author, Book

class AuthorViewSet(ViewSet):
    
    def list(self, request):
        authors = Author.selectAuthors()
        return Response(authors)

    def retrieve(self, request, pk=None):
        authors = Author.selectAuthors(id=pk)
        if authors:
            return Response(authors[0]) 
        return Response({"error": "Author not found"}, status=404)

    def create(self, request):
        authors_list = request.data
        print(authors_list)
        success = Author.insertAuthors(authors_list)
        if success:
            return Response({"message": "Authors added successfully"}, status=201)
        return Response({"error": "Error adding authors"}, status=400)

   
    @action(detail=False, methods=['put'], url_path='update')
    def update_authors(self, request):
        authors_list = request.data
        success = Author.updateAuthors(authors_list)
        if success:
            return Response({"message": "Authors updated successfully"})
        return Response({"error": "Error updating authors"}, status=400)

    @action(detail=False, methods=['delete'], url_path='delete')
    def delete(self, request):
        authors_list = request.data
        success = Author.deleteAuthors(authors_list)
        if success:
            return Response({"message": "Authors deleted successfully"})
        return Response({"error": "Error deleting authors"}, status=400)

    @action(detail=False, methods=['get'],url_path='bynationality')
    def by_nationality(self, request):
        nationality = request.query_params.get('nationality')
        if nationality:
            authors = Author.selectAuthorsByNationality(nationality)
            return Response(authors)
        return Response({"error": "Nationality parameter is required"}, status=400)
    
class BookViewSet(ViewSet):
    

    def list(self, request):
        books = Book.selectBooks()
        return Response(books)


    def retrieve(self, request, pk=None):
        books = Book.selectBooks(id=pk)
        if books:
            return Response(books[0])
        return Response({"error": "Book not found"}, status=404)
    
    def create(self, request):
        books_list = request.data
        success = Book.insertBooks(books_list)
        if success:
            return Response({"message": "Books added successfully"}, status=201)
        return Response({"error": "Error adding books"}, status=400)
    
    @action(detail=False, methods=['put'], url_path='update')
    def update_book(self, request):
        books_list = request.data
        success = Book.updateBooks(books_list)
        if success:
            return Response({"message": "Books updated successfully"})
        return Response({"error": "Error updating books"}, status=400)

    @action(detail=False, methods=['delete'], url_path='delete')
    def delete_book(self, request):
        books_list = request.data
        success = Book.deleteBooks(books_list)
        if success:
            return Response({"message": "Books deleted successfully"})
        return Response({"error": "Error deleting books"}, status=400)

    @action(detail=False, methods=['get'] ,url_path='bygenre')
    def by_genre(self, request, genre=None):
        books = Book.selectBooksByGenre(genre)
        return Response(books)
