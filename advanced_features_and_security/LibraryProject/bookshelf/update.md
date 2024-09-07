# Update the Book Title

```python
# Update the title of the book
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Verify the update
updated_book = Book.objects.get(id=retrieved_book.id)
print(updated_book.title)
