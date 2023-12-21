import requests
from colorama import Fore
import time

def send_post_request():
    url = "https://api.discord.gx.games/v1/direct-fulfillment"
    headers = {
        "origin": "https://www.opera.com",
        "Content-Type": "application/json",
        "Sec-Ch-Ua": '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
    }
    data = {
        "partnerUserId": "bc385c68-be5f-43c2-9713-cb2051fef65b"
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 429:
        print(f"Error 429: You are being rate limited by Discord!")
        return None
    else:
        print(f"Error: {response.status_code}")
        return None

def write_to_file(token_value):
    with open("codes.txt", "a") as file:
        file.write(f"https://discord.com/billing/partner-promotions/1180231712274387115/{token_value}\n")

def main():
    num_requests = 0
    try:
        num_requests = int(input("How much codes do you want to generate? "))
    except ValueError:
        print(Fore.RED + "Enter a valid integer!")
        return
    if num_requests <= 0:
        print(Fore.RED + "Enter a valid integer greater than zero!")

    for i in range(num_requests):
        response_json = send_post_request()

        if response_json:
            token_value = response_json.get("token", "")
            if token_value:
                write_to_file(token_value)
                print(Fore.GREEN + f"Request {i + 1}/{num_requests}: Token value written to codes.txt")
            else:
                print(Fore.YELLOW + f"Request {i + 1}/{num_requests}: Token value not found in the response")
        else:
            print(Fore.RED + f"Request {i + 1}/{num_requests}: Failed to get a valid response")

        # Add a delay to avoid hitting rate limits
        time.sleep(0.1)

if __name__ == "__main__":
    main()
