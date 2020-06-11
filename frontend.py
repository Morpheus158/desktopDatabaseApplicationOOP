from tkinter import Listbox, Entry, Button, Label, Tk, Scrollbar, StringVar, END
from backend import Database

database = Database()

def view_all_command():
    entries_field.delete(0, END)
    for row in database.view_all():
        entries_field.insert(END, row)

def search_entry_command():
    entries_field.delete(0, END)
    for row in database.search_entry(title_input.get(), author_input.get(), year_input.get(), isbn_input.get()):
        entries_field.insert(END, row)

def add_entry_command():
    database.add_entry(title_input.get(), author_input.get(), year_input.get(), isbn_input.get())
    entries_field.delete(0, END)
    entries_field.insert(END, (title_input.get(), author_input.get(), year_input.get(), isbn_input.get()))

def update_selected_command():
    database.update_selected(selected_row[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())


def delete_selected_command():
    database.delete_selected(selected_row[0])

def get_row(event):
    global selected_row
    row_index = entries_field.curselection()[0]
    selected_row = entries_field.get(row_index)
    title_entry.delete(0, END)
    title_entry.insert(END, selected_row[1])
    author_entry.delete(0, END)
    author_entry.insert(END, selected_row[2])
    year_entry.delete(0, END)
    year_entry.insert(END, selected_row[3])
    isbn_entry.delete(0, END)
    isbn_entry.insert(END, selected_row[4])

window = Tk()

title_label = Label(window, text="Title")
title_label.grid(row=0, column=0)

author_label = Label(window, text="Author")
author_label.grid(row=0, column=2)

year_label = Label(window, text="Year")
year_label.grid(row=1, column=0)

isbn_label = Label(window, text="ISBN")
isbn_label.grid(row=1, column=2)

title_input = StringVar()
title_entry = Entry(window, textvariable=title_input)
title_entry.grid(row=0, column=1)

author_input = StringVar()
author_entry = Entry(window, textvariable=author_input)
author_entry.grid(row=0, column=3)
#
year_input = StringVar()
year_entry = Entry(window, textvariable=year_input)
year_entry.grid(row=1, column=1)
#
isbn_input = StringVar()
isbn_entry = Entry(window, textvariable=isbn_input)
isbn_entry.grid(row=1, column=3)

view_all_button = Button(window, text="View All", width=15, command=view_all_command)
view_all_button.grid(row=2, column=3)

search_entry_button = Button(window, text="Search Entry", width=15, command=search_entry_command)
search_entry_button.grid(row=3, column=3)

add_entry_button = Button(window, text="Add Entry", width=15, command=add_entry_command)
add_entry_button.grid(row=4, column=3)

update_selected_button = Button(window, text="Update Selected", width=15, command=update_selected_command)
update_selected_button.grid(row=5, column=3)

delete_selected_button = Button(window, text="Delete Selected", width=15, command=delete_selected_command)
delete_selected_button.grid(row=6, column=3)

close_button = Button(window, text="Close", width=15, command=window.destroy)
close_button.grid(row=7, column=3)

entries_field = Listbox(window, width=30, height=9)
entries_field.grid(row=2, column=0, rowspan=6, columnspan=2)

scroll = Scrollbar(window)
scroll.grid(row=2, column=2, rowspan=6)

entries_field.configure(yscrollcommand=scroll.set)
scroll.configure(command=entries_field.yview)

entries_field.bind("<<ListboxSelect>>", get_row)

window.mainloop()