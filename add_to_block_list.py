import phantom.rules as phantom

BLOCKLIST_FILE = "/opt/phantom/data/blocklist.txt"


def add_url_to_blocklist(url: str, filename: str = BLOCKLIST_FILE) -> bool:
    """
    Adds a URL to the blocklist file.
    Returns True if successful, False otherwise.
    """

    if not url:
        phantom.debug("No URL provided to add_url_to_blocklist")
        return False

    try:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(url.strip() + "\n")

        phantom.info(f"URL added to blocklist: {url}")
        return True

    except Exception as e:
        phantom.error(f"Failed to add URL to blocklist: {e}")
        return False
