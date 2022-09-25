import re
import markdown2
from markdown2 import Markdown
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
markdowner = Markdown()


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
    default_storage.save(filename, ContentFile(content))


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    try:
        f = default_storage.open(f"entries/{title}.md")
        f = f.read().decode("utf-8")
        fr = markdowner.convert(f)

        return fr
        
    except FileNotFoundError:
        return None

def search_entry(name):
    list_name = list_entries()
    if name.upper() in list_name or name.lower() in list_name or name.title() in list_name:
        return name
    elif any(name.title() in string or name.lower() in string or name.upper() in string for string in list_name):
        res = [string for string in list_name if name.title() in string or name.lower() in string or  name.title() in string]
        return res
    else:
        return []

def edit_entry(title):
    try:
        f = default_storage.open(f"entries/{title}.md")
        f = f.read().decode("utf-8")
        return f
        
    except FileNotFoundError:
        return None

