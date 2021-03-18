![Build](https://github.com/julb/action-post-twitter-status/workflows/Build/badge.svg)

# GitHub Action to Post a status on Twitter

The GitHub Action for posting a message on your Twitter account.

The pre-requisite is to create a Twitter application [here](https://developer.twitter.com/apps).
Once it is done, you need to retrieve your API keys and Access Token of your Twitter application.
Finally, register them as secrets in Github :

- `TWITTER_APP_CONSUMER_API_KEY` : the API key.
- `TWITTER_APP_CONSUMER_API_SECRET_KEY` : the API secret key.
- `TWITTER_APP_ACCESS_TOKEN` : the access token.
- `TWITTER_APP_ACCESS_TOKEN_SECRET` : the access token secret.

## Usage

### Example Workflow file

- Post a status message a twitter:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Post Twitter Status
        uses: julb/action-post-twitter-status@v1
        with:
          message: "Hello from Github Action!"
          twitter_app_consumer_api_key: ${{ secrets.TWITTER_APP_CONSUMER_API_KEY }}
          twitter_app_consumer_api_secret_key: ${{ secrets.TWITTER_APP_CONSUMER_API_SECRET_KEY }}
          twitter_app_access_token: ${{ secrets.TWITTER_APP_ACCESS_TOKEN }}
          twitter_app_access_token_secret: ${{ secrets.TWITTER_APP_ACCESS_TOKEN_SECRET }}
```

### Inputs

| Name                                  | Type   | Default   | Description                                                   |
| ------------------------------------- | ------ | --------- | ------------------------------------------------------------- |
| `message`                             | string | `Not set` | Message to post to Twitter. **Required**                      |
| `twitter_app_consumer_api_key`        | string | `Not Set` | The Twitter application consumer API key. **Required**        |
| `twitter_app_consumer_api_secret_key` | string | `Not Set` | The Twitter application consumer API secret key. **Required** |
| `twitter_app_access_token`            | string | `Not Set` | The Twitter application access token. **Required**            |
| `twitter_app_access_token_secret`     | string | `Not Set` | The Twitter application access token secret. **Required**     |

**Important note**: Twitter credentials are sensitive values and should be provided using Github Action Secrets.
Don't paste your credentials in clear in your Github action.

### Outputs

| Name | Type   | Description                  |
| ---- | ------ | ---------------------------- |
| `id` | number | ID of the status (the tweet) |

## Contributing

This project is totally open source and contributors are welcome.

When you submit a PR, please ensure that the python code is well formatted and linted.

```
$ make install.dependencies
$ make format
$ make lint
```
