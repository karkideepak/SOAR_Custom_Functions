def on_start(container):
    url = phantom.prompt(
        container=container,
        user="admin",
        message="Enter the URL to block",
        respond_in_mins=30
    )

    add_url_to_blocklist(url)

    return
