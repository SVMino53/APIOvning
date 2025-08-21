import requests
from requests.exceptions import Timeout
import json


def get_response(url : str) -> requests.Response | None:
    try:
        r = requests.get(url=url, timeout=5)
        r.raise_for_status()
    except Timeout:
        print("Request tog för lång tid och avbröts")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"HTTP-fel: {e}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Ett fel uppstod: {e}")
        return None
    else:
        print("Request succeeded")
        return r
    
def save_raw_data(response: requests.Response, filename: str) -> None:
    with open(f"raw/{filename}.json", "w") as f:
        data = response.json()
        f.write(json.dumps(data, indent=4))

def main() -> None:
    r = get_response("https://data.tomelilla.se/rowstore/dataset/3617552e-4c28-4a46-9b74-ac8bbbfee33f")
    #r = get_response("Canada")
    if r is not None:
        save_raw_data(r, "users")
        print("Data sparad i raw/users.json")
    else:
        print("Ingen data sparad")


if __name__ == "__main__":
    main()