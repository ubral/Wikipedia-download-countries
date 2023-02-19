# Import the necessary libraries
import requests
from bs4 import BeautifulSoup
import pandas as pd
import lxml

# Define the Wikipedia URL and table class
wikiurl = "https://en.wikipedia.org/wiki/List_of_ISO_3166_country_codes"
table_class = "wikitable sortable jquery-tablesorter"

# Send a GET request to the Wikipedia page and print the status code to check if the request is successful
response = requests.get(wikiurl)
print(response.status_code)

# Parse the HTML content of the response with BeautifulSoup and find the table with the specified class
soup = BeautifulSoup(response.text, 'html.parser')
table = soup.find('table', {'class': "wikitable"})

# Use Pandas' read_html function to extract the table from the HTML and convert it into a DataFrame
df = pd.read_html(str(table))
df = pd.DataFrame(df[0])

# Rename the columns of the DataFrame using a list comprehension and an if statement to handle columns with two words
df.columns = [f"{c[0]} {c[1]}" if isinstance(c, tuple) else c for c in df.columns]

# Create a dictionary to map old column names to new column names, keeping only the last word of each column name
col_map = {col: col.split()[-1] for col in df.columns}

# Use the rename() method to update the column names of the DataFrame with the dictionary
df = df.rename(columns=col_map)

# Print the first five rows of the updated DataFrame
print(df.head())



