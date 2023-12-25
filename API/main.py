import requests
from config import Config
import math


def get_auth_id() -> str:
    try:
        r = requests.get(url=Config.AUTH_URL, timeout=10, headers=Config.headers, cookies=Config.cookies)
        if r.status_code == 200:
            if 'model' in r.json():
                if 'auth' in r.json()['model']:
                    auth_id = r.json()['model']['auth']

                    return auth_id

    except requests.exceptions.Timeout as t:
        print(t)
        get_auth_id()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_balance() -> float:
    auth_id = get_auth_id()
    try:
        url = f"https://my.firstvds.ru/billmgr?auth={auth_id}&out=json&func=whoami"
        r = requests.get(url=url, timeout=10, headers=Config.headers, cookies=Config.cookies)
        if r.status_code == 200:
            if 'doc' in r.json():
                if 'user' in r.json()['doc']:
                    if '$balance' in r.json()['doc']['user']:
                        balance = r.json()['doc']['user']['$balance']

                        if balance:
                            return float(balance)

    except requests.exceptions.Timeout as t:
        print(t)
        get_balance()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_exp_days():
    one_day_price = 35.45
    balance = get_balance()

    day_exp = math.floor(balance / one_day_price)

    print(day_exp)


if __name__ == '__main__':
    get_exp_days()