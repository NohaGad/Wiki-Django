# Wiki Django

![Django](https://img.shields.io/badge/Django-3.2-blue)
![Python](https://img.shields.io/badge/Python-3.9-blue)
![Markdown2](https://img.shields.io/badge/Markdown2-2.4.0-green)

Wiki Django is a web application that allows users to create, view, search, edit, and explore encyclopedia entries. It provides features such as viewing individual encyclopedia entries, searching for entries, creating new entries, editing existing entries, and browsing random entries.

## Features

- **Entry Page:** Visiting `/wiki/TITLE` displays the contents of the encyclopedia entry with the specified title. If the entry does not exist, an error page is displayed.
- **Index Page:** Update `index.html` to allow users to click on entry names to be taken directly to the entry page.
- **Search:** Users can type a query into the search box to search for encyclopedia entries. Matching entries are displayed directly, while non-matching queries result in a search results page displaying entries with the query as a substring.
- **New Page:** Clicking "Create New Page" allows users to create a new encyclopedia entry by entering a title and Markdown content.
- **Edit Page:** Users can edit existing entries by clicking a link on the entry page. The Markdown content is pre-populated in a textarea for editing.
- **Random Page:** Clicking "Random Page" takes users to a random encyclopedia entry.
- **Markdown to HTML Conversion:** Markdown content in entry files is converted to HTML before being displayed.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/NohaGad/Wiki-Django.git

2. Run the server:

   ```bash
   python manage.py runserver

3. Access the application in a web browser at `http://127.0.0.1:8000/`.

## Usage
- **View Entries** : Visit /wiki/TITLE to view the content of a specific encyclopedia entry.
- **Search** : Type a query into the search box to search for encyclopedia entries.
- **Create New Page** : Click "Create New Page" in the sidebar to create a new encyclopedia entry.
- **Edit Page** : Click "Edit" on an entry page to edit the content of that entry.
- **Random Page** : Click "Random Page" in the sidebar to navigate to a random encyclopedia entry.

## Contributing
Contributions are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.




