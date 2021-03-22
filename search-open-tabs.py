#! python3
# search-open-tabs.py
# A small script to open the top search results from Google in tabs

import bs4,requests, sys, webbrowser

# Display text while searching for results
print("Searching...") 

# Get the web page of the Google search with command line arguments
res = requests.get("https://google.be/search?q=" + " ".join(sys.argv[1:]))

# Check status of HTTP request
res.raise_for_status()

# Retrieve top search result links.
soup = bs4.BeautifulSoup(res.text, "html.parser")

# Open a browser tab for each result    
for g in soup.find_all("div", class_= "yuRUbf"):
    anchors = g.find_all("a")
    for i in range(0, 5):
        linkToOpen = anchors[i]["href"]
        title = g.find("h3").text
        print("Opening" + title)
        webbrowser.open(linkToOpen)