import json
import os

data_file = "library.txt"

# load data 
def load_library():
    if os.path.exists(data_file):
        with open(data_file , "r") as file:
            return json.load(file)
    return []

#saving data
def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library,file)
    

# add books    
def add_books(library):
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    year = input("Enter the published year of the book:")
    genre = input("Enter the genre of the book: ")
    readStatus = input ("Did you read the book? (Yes/No): ").lower()== "yes"

    new_book = {
        "title"  : title,
        "author" : author,
        "year"  : year,
        "genre" : genre,
        "read" : readStatus
    }

    library.append(new_book)
    save_library(library)
    print(f"Book {title} by {author} added successfully!")


# remove book
def remove_book(library):
    title = input("Enter the title of the book to remove:").lower()
    initial_length = len(library)
    library = [book for book in library if book ["title"].lower() != title]

    if len(library) < initial_length:
        save_library(library)
        print(f"Book {title} has been removed from the library.")

    else:
        print(f"Book {title} not found in the library.")  
    return library


# search book
def search_book(library):
    print("Search by title, author, year, genre")
    search_by = input("Enter the field to search by:")

    if search_by not in ['title', 'author', 'year', 'genre']:
        print("Invalid field. please try again")
        return
    
    search_term = input(f"Enter the {search_by} to search for:").lower()

    result = [book for book in library if search_term in book[search_by].lower()]

    if result:
       print(f"Found {len(result)} result(s):")
       for book in result:
           print(f"- {book['title']} by {book['author']} in {book['year']} - [{book['genre']}]")

    else:
        print("No book found matching your search field.")



# display read status
def display_status(library):
    if library:
        for book in library:
            status = "read" if book['read'] else "unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}.")
        
    else:
        print("The library has no books.")


# display statistics
def display_statistics(library):
    total_books = len(library)
    read_books = len([book for book in library if book['read']])

    percentage_books = (read_books / total_books) * 100 if total_books > 0 else 0

    print(f"Total Books: {total_books}.")
    print(f"Read Books: {read_books}.")
    print(f"Percentage of read books is: {percentage_books:.2f}%.")

# Main program
def main():
    library = load_library()

    while True:
        print("\n MENU ( This is case sensitive. Please use lower case to search)")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Search a Book")
        print("4. Display all Book")
        print("5. Display Statistics")
        print("6. Exit")

        option = input("Enter your option:")

        if option == '1':
            add_books(library)

        elif option == '2':
            library = remove_book(library)

        elif option == '3':
            search_book(library)   

        elif option == '4':
            display_status(library)

        elif option == '5':
            display_statistics(library)

        elif option == '6':
            print("Thank you for exploring the library. GOODBYE!")         
            break

        else:
            print("Invalid Option. Please choose correct option.")


if __name__ == '__main__':
    main()
    
         




    
