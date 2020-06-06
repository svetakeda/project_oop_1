from book import Book
def read_file(file_name):
    books = []
    with open(file_name) as file:
        lines = file.read().splitlines()     # считывает весь файл
        for line in lines:
            a = line.split(';')
            name = a[0]
            year = int(a[1])
            author = a[2]
            cost = int(a[3])
            book = Book(name, year, author, cost)
            books.append(book)
    return books

def find_max(books):
    max = books[0]
    for book in books:
        if book.cost > max.cost:
            max = book
    return max

def sort_books(books):
    books.sort(key=lambda book: book.cost)

def find_author(books):
    author = input('Введите автора: ')
    for i in range(len(books)):
        if books[i] == author:
            print(i)




def main():
    file_name = input('Введите имя файла: ')
    books = read_file(file_name)
    print(books)
    max_book = find_max(books)
    print('Самая дорогая книга  в магазине: ', max_book)
    sort_books(books)
    print(books)
    print(find_author(books))
main()
