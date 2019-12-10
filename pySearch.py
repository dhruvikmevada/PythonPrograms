''' Date: 3/12/2019
    Developer: Dhruvik Mevada <cyb3rsky@gmail.com>
    
    Description: This program takes input as of what you want to search and opens it directy in browser. More updates comming soon.
''' 

import webbrowser

def playvideo(search_query):  # Function for youtube search

    url = 'https://www.youtube.com/search?q=' + search_query
    webbrowser.open(url)

def search_content(search_query):  # Function for google search

    url = 'https://www.google.com/search?q=' + search_query
    webbrowser.open(url)

def search_game(search_query):  # Function for steam search
    url = 'https://store.steampowered.com/search/?term=' + search_query
    webbrowser.open(url)

if __name__ == "__main__":
    
    ask_to_search = input('What do you want to search fo? \n1) Youtube \n2) Google \n3) Steam\n...')

    if ask_to_search == '1':
        title = input('Enter the title: ')
        playvideo(title)

    elif ask_to_search == '2':
        title = input('Enter the title: ')
        search_content(title)

    elif ask_to_search == '3':
        title = input('Enter the title: ')
        search_content(title)

    else:
        print('Wrong Input')
