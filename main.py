import requests
import time


class APIClient:

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token

    @property
    def headers(self):

        headers = {
            "Host": "api.asmodee.net",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "sv-SE,sv;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate, br",
            "Authorization": self.bearer_token,
            "Origin": "https://account.asmodee.net",
            "DNT": "1",
            "Connection": "keep-alive",
            "Referer": "https://account.asmodee.net/en/game/TerraformingMars/history",
            "TE": "Trailers"
        }
        return headers

    def fetch_last_games(self, player_id):
        url = f"https://api.asmodee.net/main/v1/user/{player_id}/lastgames/TerraformingMars"

        player_data = []

        offset = 0

        while True:

            params = {
                "limit": 100,
                "status": "ended,disconnected",
                "o": 0,
                "offset": offset,
            }

            data = requests.get(url, headers=self.headers, params=params).json()

            offset += 100

            if not data["data"]["games"]:
                break

            player_data = player_data + data['data']['games']

            time.sleep(2)

        return player_data

    def fetch_games(self, player_id):
        url = f"https://api.asmodee.net/main/v1/user/{player_id}/games/TerraformingMars"

        player_data = []

        years = range(2017, 2021)

        for year in years:
            offset = 0
            while True:

                params = {
                    "limit": 100,
                    "status": "ended,disconnected",
                    "o": 0,
                    "offset": offset,
                    "y": year
                }

                data = requests.get(url, headers=self.headers, params=params).json()

                offset += 100

                if not data["data"]["games"]:
                    break

                player_data = player_data + data['data']['games']

                time.sleep(2)

        return player_data

    def get_player_games(self, player_id):
        return self.fetch_games(player_id) + self.fetch_last_games(player_id)

    def get_player_rank(self, player_id):
        api_url = f"https://api.asmodee.net/main/v1/user/{player_id}/rank/TerraformingMars"
        return requests.get(api_url, headers=self.headers).json()

    def get_ranks(self, limit=20, offset=0):
        api_url = f"https://api.asmodee.net/main/v1/game/TerraformingMars/rank/established"

        params = {
            "offset": offset,
            "limit": limit
        }

        return requests.get(api_url, headers=self.headers, params=params).json()


