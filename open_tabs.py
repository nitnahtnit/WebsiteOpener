import webbrowser
import time

url_list = [
    'https://www.youtube.com',
    'https://www.hotmail.com',
    'https://www.codeproject.com',
    'https://www.github.com'
]

def openpages():
    for url in url_list:
        webbrowser.open(url, 2, False)
        time.sleep(2)   # sleep between otherwise will open in seperate windows..

openpages()
