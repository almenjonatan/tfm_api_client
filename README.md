# Asmodee/TFM api client

## Installation

```
pip install tfm-client
```

## Usage

```python 
from tfm_client import APIClient

bearer = "Bearer TOKEN from asmoodee"

api_client = APIClient(bearer)

player_id = 111111

games = api_client.get_player_games(player_id)

```
