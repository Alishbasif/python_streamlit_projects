import streamlit as st
import json
import os

data_file = "library.txt"

# --- Load & Save Library ---
def load_library():
    if os.path.exists(data_file):
        with open(data_file, "r") as file:
            return json.load(file)
    return []

def save_library(library):
    with open(data_file, "w") as file:
        json.dump(library, file, indent=2)

# --- Add Book ---
def add_book(library, title, author, year, genre, read_status):
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read_status
    }
    library.append(new_book)
    save_library(library)
    st.success(f"Book added: {title} by {author}")

# --- Remove Book ---
def remove_book(library, title):
    title_lower = title.lower()
    new_library = [book for book in library if book["title"].lower() != title_lower]
    if len(new_library) < len(library):
        save_library(new_library)
        st.success(f"Book removed: {title}")
    else:
        st.warning(f"Book not found: {title}")
    return new_library

# --- Search Book ---
def search_books(library, field, term):
    field = field.lower()
    term = term.lower()
    if field not in ["title", "author", "year", "genre"]:
        st.error("Invalid search field")
        return []
    results = [book for book in library if term in str(book[field]).lower()]
    return results

# --- Display Library ---
def display_library(library):
    if library:
        for book in library:
            status = "Read" if book["read"] else "Unread"
            st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        st.info("Library is empty")

# --- Display Statistics ---
def display_statistics(library):
    total = len(library)
    read_count = len([b for b in library if b["read"]])
    percent_read = (read_count / total * 100) if total else 0
    st.write(f"**Total books:** {total}")
    st.write(f"**Books read:** {read_count}")
    st.write(f"**Percentage read:** {percent_read:.2f}%")

# --- Streamlit App ---
st.title("📚 Personal Library Manager")

library = load_library()

menu = ["Add Book", "Remove Book", "Search Book", "Display Library", "Statistics"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Add Book":
    st.subheader("Add a New Book")
    with st.form("add_form"):
        title = st.text_input("Title")
        author = st.text_input("Author")
        year = st.text_input("Year")
        genre = st.text_input("Genre")
        read_status = st.checkbox("Have you read this book?")
        submitted = st.form_submit_button("Add Book")
        if submitted:
            if title and author:
                add_book(library, title, author, year, genre, read_status)
                library = load_library()
            else:
                st.warning("Title and Author are required!")

elif choice == "Remove Book":
    st.subheader("Remove a Book")
    remove_title = st.text_input("Enter the title of the book to remove")
    if st.button("Remove"):
        library = remove_book(library, remove_title)

elif choice == "Search Book":
    st.subheader("Search Books")
    field = st.selectbox("Search by", ["title", "author", "year", "genre"])
    term = st.text_input("Search term")
    if st.button("Search"):
        results = search_books(library, field, term)
        if results:
            st.success(f"Found {len(results)} result(s):")
            display_library(results)
        else:
            st.warning("No books found.")

elif choice == "Display Library":
    st.subheader("All Books in Library")
    display_library(library)

elif choice == "Statistics":
    st.subheader("Library Statistics")
    display_statistics(library)
