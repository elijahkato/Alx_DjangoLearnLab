# Delete the Book

```python
# Delete the book
retrieved_book.delete()

# Verify the deletion
all_books = Book.objects.all()
print(all_books)
