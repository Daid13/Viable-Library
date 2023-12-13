from viablelibrary import ViableLibrary
def create_values(lib):
    books=[["Return of the King","The finale to the epic, genre defining work by J.R.R. Tolkien."],
           ["Foundation", "The Galactic Empire is dying but Hari Seldon's Psychohistory predicts a better future."],
           ["Artemis Fowl", "Teenage criminal mastermind begins to pray on the fay, but does he bite off more than he chew?"]]
    for b in books:
        lib.add_book(b[0],b[1])


lib=ViableLibrary()
create_values(lib)
print(lib.get_available_books())
print(lib.register("John", "Smith", "johnsmith@mail.com","pass"))
print(lib.login("johnsmith@mail.com", "pass"))
print(lib.borrow("Foundation"))
print(lib.get_book_list())
print(lib.get_available_books())
print(lib.get_loaned_books())            

