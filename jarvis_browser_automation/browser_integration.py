import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from jarvis_browser_automation.open_website import *
from jarvis_browser_automation.tab_automation import *
from jarvis_browser_automation.scroll_automation import *
from jarvis_browser_automation.search import *

def browser_cmd(query):
    query = query.lower().strip()

    if "open" in query:
        if "website" in query or "site" in query:
            query = query.replace("open ", "").replace("website", "").replace("site", "").strip()
            openWeb(query)
        elif "new tab" in query:
            new_tab()
        elif "new window" in query:
            new_window()
        elif "private" in query:
            private_tab()
        elif "downloads" in query:
            open_downloads()
        elif "bookmarks" in query:
            open_bookmarks()
        elif "history" in query:
            open_history()
        elif "dev tools" in query:
            open_dev_tools()
        elif "browser menu" in query:
            browser_menu()

    elif "close tab" in query:
        close_tab()

    elif "refresh" in query:
        refresh_page()

    elif "zoom in" in query:
        zoom_in()

    elif "zoom out" in query:
        zoom_out()

    elif "next tab" in query or "switch tab" in query:
        next_tab()

    elif "previous tab" in query or "back tab" in query:
        prev_tab()

    elif "go back" in query:
        go_back()

    elif "go forward" in query:
        go_forward()

    elif "full screen" in query:
        full_screen()

    elif "scroll up" in query:
        scroll_up()

    elif "scroll down" in query:
        scroll_down()

    elif "scroll to top" in query:
        scroll_to_top()

    elif "scroll to bottom" in query:
        scroll_to_bottom()

    elif query.startswith("search"):
        query = query.replace("search", "").replace("on google", "").strip()
        search_google(query)
    else:
        pass

# query = "search Arijit Singh "
# browser_cmd(query)