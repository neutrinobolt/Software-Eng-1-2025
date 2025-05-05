#!usr/bin/env/python3

"""music player for Youtube.
Contains: music player function"""

import webbrowser

def play_yt(link_file: str):

    # print(f"Reading from file", {link_file}) #debug
    # Get link
    with open(link_file, mode='r', encoding='utf-8') as url_file:
        # print(f"url_file: ", {url_file}) #debug
        url_file.seek(0)
        if url_file.read() == "none":
            # print("No link given.") #debug
            link_url = None
        else:
            url_file.seek(0)
            link_url = url_file.read()
            # print(f"Url: ", {link_url}) #debug
    # Play given link
    if link_url is not None:
        webbrowser.open(link_url)

    

if __name__ == "__main__":
    play_yt()
