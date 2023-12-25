import requests
from config import Config
import math
import discord
import logging

logging.basicConfig(level=logging.INFO)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


def get_auth_id() -> str:
    try:
        logging.info("--->   receiving auth_id")
        r = requests.post(url=Config.AUTH_URL, timeout=5, json=Config.AUTH_DATA)
        logging.info(r.json())
        if r.status_code == 200:
            if 'data' in r.json():
                if 'auth_key' in r.json()['data']:
                    auth_id = r.json()['data']['auth_key']
                    logging.info(f"--->   auth_id received: {auth_id}")

                    return auth_id

    except requests.exceptions.Timeout as t:
        print("The request timed out after 5 seconds.")
        get_auth_id()
    except requests.exceptions.RequestException as e:
        raise SystemExit(e)


def get_balance() -> float:
    auth_id = get_auth_id()
    try:
        logging.info("--->   receiving balance")
        url = f"https://my.firstvds.ru/billmgr?auth={auth_id}&out=json&func=whoami"
        r = requests.get(url=url, timeout=5)
        logging.info(r.json())
        if r.status_code == 200:
            if 'doc' in r.json():
                if 'user' in r.json()['doc']:
                    if '$balance' in r.json()['doc']['user']:
                        balance = r.json()['doc']['user']['$balance']
                        logging.info(f"--->   balance received: {balance}")

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
    logging.info("--->   calculate exp days")
    day_exp = math.floor(balance / one_day_price)
    logging.info(f"--->   exp days calculated: {day_exp}")

    return day_exp


@client.event
async def on_ready():
    day_exp = get_exp_days()
    template = f"Оплаченных дней: {day_exp}"

    logging.info("--->  write exp days to discord")

    channel_balance = client.get_channel(Config.DISCORD_CHANNEL_ID)
    # await channel_balance.send("test")
    msg = await discord.utils.get(channel_balance.history())
    if msg:
        async for message in channel_balance.history():
            await message.edit(content=template)
            await client.close()


client.run(Config.BOT_TOKEN)
