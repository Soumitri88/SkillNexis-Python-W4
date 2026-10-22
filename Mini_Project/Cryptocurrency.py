#Write a program to fetch live cryptocurrency prices.

import requests
from datetime import datetime

API_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_prices():
    coins = "bitcoin,ethereum,solana,ripple,dogecoin"

    params = {
        "ids": coins,
        "vs_currencies": "usd,inr",
        "include_24hr_change": "true"
    }

    try:
        response = requests.get(API_URL, params=params, timeout=15)
        response.raise_for_status()
        data = response.json()

        coin_names = {
            "bitcoin": "Bitcoin (BTC)",
            "ethereum": "Ethereum (ETH)",
            "solana": "Solana (SOL)",
            "ripple": "XRP",
            "dogecoin": "Dogecoin (DOGE)"
        }

        print("\n========== LIVE CRYPTO PRICES ==========")
        print("Updated at:", datetime.now().strftime("%d-%m-%Y %H:%M:%S"))
        print("-" * 65)

        print(f"{'Cryptocurrency':<22} {'Price (USD)':>15} {'Price (INR)':>20}")
        print("-" * 65)

        for coin_id, name in coin_names.items():
            if coin_id in data:
                usd = data[coin_id].get("usd")
                inr = data[coin_id].get("inr")

                print(f"{name:<22} ${usd:>14,.2f} ₹{inr:>18,.2f}")

                change = data[coin_id].get("usd_24h_change")
                if change is not None:
                    print(f"  24-hour change: {change:+.2f}%")

        print("=" * 65)

    except requests.exceptions.HTTPError as error:
        print("API request failed:", error)
        print("Check the API response and your rate limits.")

    except requests.exceptions.RequestException as error:
        print("Network error:", error)

    except (ValueError, TypeError, KeyError) as error:
        print("Could not process the API data:", error)


while True:
    get_crypto_prices()

    choice = input("\nPress Enter to refresh, or type 'exit' to quit: ")

    if choice.strip().lower() == "exit":
        print("Crypto tracker closed.")
        break
