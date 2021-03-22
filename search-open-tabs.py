#! python3
# A small script to open the top search results from Google in tabs

import bs4,requests, sys, webbrowser

# Display text while searching for results
print("Searchig...") 

# Get the web page of the Google search with command line arguments
res = requests.get("https://google.be/search?q=" + " ".join(sys.argv[1:]))

# Check status of HTTP request
res.raise_for_status()

# TODO: Retrieve top search result links.
# TODO: Open a browser tab for each result
