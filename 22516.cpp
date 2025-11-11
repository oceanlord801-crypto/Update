books = [
    {"id": 5, "name": "Chava"},
    {"id": 10, "name": "the untold story"},
    {"id": 3, "name": "Steve Jobs"},
    {"id": 8, "name": "Deep Work"},
    {"id": 1, "name": "Tim Cook"},
]


def linear_search(books, key_id):
    for book in books:
        if book["id"] == key_id:
            return book
    return None


def binary_search(books_sorted, key_id):
    low = 0
    high = len(books_sorted) - 1

    while low <= high:
        mid = (low + high) // 2
        if books_sorted[mid]["id"] == key_id:
            return books_sorted[mid]
        elif books_sorted[mid]["id"] < key_id:
            low = mid + 1
        else:
            high = mid - 1
    return None


books_sorted = sorted(books, key=lambda x: x["id"])

search_id = int(input("Enter Book ID that you want to search: "))


print("\n[Linear Search]")
result1 = linear_search(books, search_id)
if result1:
    print(f"Book Found: ID = {result1['id']}, Name = '{result1['name']}'")
else:
    print("Book not found")

print("\n[Binary Search]")
result2 = binary_search(books_sorted, search_id)
if result2:
    print(f"Book Found: ID = {result2['id']}, Name = '{result2['name']}'")
else:
    print("Book not found")
