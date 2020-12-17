import requests
import time


class APIClient:

    def __init__(self, bearer_token):
        self.bearer_token = bearer_token
        self.base_url = "https://api.asmodee.net"

    @property
    def headers(self):

        headers = {
            "Host": "tfm_api_client.asmodee.net",
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

    def get_player_games(self, player_id: int):
        urls = [
            f"/main/v1/user/{player_id}/lastgames/TerraformingMars?limit=100&status=ended,disconnected&o=0&offset=0",
            f"/main/v1/user/{player_id}/games/TerraformingMars?limit=100&status=ended,disconnected&o=0&offset=0"
        ]

        player_data = []

        for url in urls:

            url = self.base_url + url

            while True:

                data = requests.get(url, headers=self.headers).json()

                player_data = player_data + data['data']['games']

                if "next" not in data["data"]["_links"]:
                    break

                url = self.base_url + data["data"]["_links"]["next"].split(".net")[-1]

                time.sleep(2)

        return player_data

    def get_player_rank(self, player_id):
        api_url = f"{self.base_url}/main/v1/user/{player_id}/rank/TerraformingMars"
        return requests.get(api_url, headers=self.headers).json()

    def get_ranks(self, limit=20, offset=0):
        api_url = f"{self.base_url}/main/v1/game/TerraformingMars/rank/established"

        params = {
            "offset": offset,
            "limit": limit
        }

        return requests.get(api_url, headers=self.headers, params=params).json()

    def get_all_ranks(self):
        url = f"{self.base_url}/main/v1/game/TerraformingMars/rank/established?limit=100&o=0&offset=0"

        ranks = []

        while True:

            data = requests.get(url, headers=self.headers).json()

            ranks = ranks + data['data']['ranks']

            if "next" not in data["data"]["_links"]:
                return ranks

            print("Fetching: " + url)

            url = self.base_url + data["data"]["_links"]["next"].split(".net")[-1]

            time.sleep(1)
