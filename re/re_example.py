import re
from bs4 import BeautifulSoup, MarkupResemblesLocatorWarning

def clean_text(text):
    text = BeautifulSoup(text, 'html.parser').get_text() # Remove html tags
    text = re.sub("http[s]?\:\/\/\S+", " ", text) # Remove links
    text = re.sub("[ \t\n]+", " ", text) # Remove tabs, newlines and multiple spaces
    text = re.sub("[^a-zA-Z]", " ", text) 
    
    return text.strip().lower()