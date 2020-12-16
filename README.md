# Asmodee/TFM api client

## Installation

```
pip install tfm-api-client
```

## Usage

```python 
from tfm_api_client import APIClient

bearer_token = "Bearer token from asmodee web page"

client = APIClient(bearer_token)

player_id = 1111111

games = client.get_player_games(player_id)

```
