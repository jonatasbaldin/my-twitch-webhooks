import aiohttp
from sanic import response, Sanic

from settings import (
    CALLBACK_URL,
    PORT,
    LAST_FOLLOWER_FILE,
    TWITCH_API_URL,
    TWITCH_APP_CLIENT_ID,
    TWITCH_LEASE_SECONDS,
    TWITCH_USER_ID,
)


app = Sanic()


@app.listener('before_server_start')
async def initialize_webhook(app, loop):

    twitch_data = {
        'hub.callback': CALLBACK_URL,
        'hub.mode': 'subscribe',
        'hub.topic': f'{TWITCH_API_URL}/users/follows?first=1&to_id={TWITCH_USER_ID}',
        'hub.lease_seconds': TWITCH_LEASE_SECONDS,
    }

    async with aiohttp.ClientSession(headers={'Client-Id': TWITCH_APP_CLIENT_ID}) as session:
        async with session.post(f'{TWITCH_API_URL}/webhooks/hub', json=twitch_data) as r:
            return await r.text()


@app.route('/', methods=['GET', 'POST'])
async def root(request):
    challenge = request.args.get('hub.challenge')
    if challenge:
        return response.text(challenge)

    if request.json:
        data = request.json.get('data')
        if len(data) > 0:
            write_username_to_file(data[0].get('from_name'))

    return response.text('')


def write_username_to_file(username):
    with open(LAST_FOLLOWER_FILE, 'w+t') as file:
        file.write(username)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
