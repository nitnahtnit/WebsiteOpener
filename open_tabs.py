import webbrowser

url_list = [
    'https://www.youtube.com',
    'https://www.hotmail.com',
    'https://www.codeproject.com',
    'https://www.github.com'
]

def openpages():
    for url in url_list:
        webbrowser.open_new_tab(url)

openpages()