#! python3
# librarySearch.py - launches 3 webpages on KCLS, Sno-Isle, and SPL libraries
# that search for the book types in

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # get address from command line
    address = ' '.join(sys.argv[1:])
else:
    # get address from clipboard
    address = pyperclip.paste()

if sys.argv[1] == 'ebook':
    type = 'f_FORMAT=EBOOK&'
elif sys.argv[1] == 'audiobook':
    type = 'f_FORMAT=AB&'
else:
    type = ''

# kcls
webbrowser.open('https://kcls.bibliocommons.com/v2/search?' + type + 'query='
                + address + '&searchType=keyword')

# sno-isle
webbrowser.open('https://sno-isle.bibliocommons.com/v2/search?' + type + 'query='
                + address + '&searchType=keyword')

# spl
webbrowser.open('https://seattle.bibliocommons.com/v2/search?' + type + 'query='
                + address + '&searchType=keyword')
