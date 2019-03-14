def write_username_to_file(username):
    with open(LAST_FOLLOWER_FILE, 'w+t') as file:
        file.write(username)
