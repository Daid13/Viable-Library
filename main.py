from viablelibrary import ViableLibrary
import jinja2

environment = jinja2.Environment(loader=jinja2.FileSystemLoader("templates/"))

def create_values(lib):
    books=[["Return of the King","The finale to the epic, genre defining work by J.R.R. Tolkien."],
           ["Foundation", "The Galactic Empire is dying but Hari Seldon's Psychohistory predicts a better future."],
           ["Artemis Fowl", "Teenage criminal mastermind begins to pray on the fay, but does he bite off more than he chew?"]]
    for b in books:
        lib.add_book(b[0],b[1])


lib=ViableLibrary()
create_values(lib)
display_template = environment.get_template("start.html")
display_template.render()


