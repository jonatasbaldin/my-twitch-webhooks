from os import getenv
from pathlib import Path


TWITCH_API_URL = 'https://api.twitch.tv/helix'
TWITCH_USER_ID = getenv('TWITCH_USER_ID')
TWITCH_APP_CLIENT_ID = getenv('TWITCH_APP_CLIENT_ID')
TWITCH_LEASE_SECONDS = getenv('TWITCH_LEASE_SECONDS', '864000')

CALLBACK_URL = getenv('CALLBACK_URL')
PORT = int(getenv('PORT', 8000))

LAST_FOLLOWER_FILE = f'{str(Path.home())}/last_follower.txt'
