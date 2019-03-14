# My Twitch Webhooks ✨
My personal app to handle Twitch webhooks.

## Features
- Writes the last follower username to `$HOME/last_follower.txt` to be used as a source to OBS.

## Using it
Install [Poetry](https://github.com/sdispater/poetry).

Create a new [Twitch Application](https://dev.twitch.tv/console/apps/create) and note its Client ID.

Define a environment variables file – `.env` – with the following content:
```bash
export TWITCH_USER_ID=<your user id>
export TWITCH_APP_CLIENT_ID=<your app client id>
export CALLBACK_URL=<the external address to receive the webhooks, ngrok maybe?>
```

If you don't have a external address, use [ngrok](https://ngrok.com/):
```bash
ngrok http 8000
```

And use the `https://<your address>.ngrok.io` as the `CALLBACK_URL`.

Export the variables:
```bash
source .env
```

Install the dependencies:
```bash
poetry install
```

Run the app:
```bash
poetry run python app.py
```

## License
[MIT](https://github.com/jonatasbaldin/my-twitch-webhooks/blob/master/LICENSE).