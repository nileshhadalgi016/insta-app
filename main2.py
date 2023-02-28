import instaloader
import random

# Read the list of proxies from the file
with open('http_proxies.txt', 'r') as f:
    proxies = f.read().splitlines()

# Choose a random proxy from the list, or use a direct connection if the list is empty
proxy = random.choice(proxies) if proxies else None

# Create an instance of Instaloader with the default settings
L = instaloader.Instaloader()

# If a proxy was chosen, set the proxies attribute of the session object
if proxy:
    L.context._session.proxies = {"https": proxy, "http": proxy}

# Loop until we successfully load the Instagram profile
while True:
    try:
        # Load the Instagram profile and get the followers
        print(f"Using proxy {proxy}")
        followers = instaloader.Profile.from_username(L.context, "instagram").followers

        # Print the list of followers and break out of the loop
        print(followers)
        break
    except instaloader.exceptions.ConnectionException:
        # If the operation fails due to a connection error, try a new proxy
        if proxies:
            new_proxy = random.choice(proxies)
            print(f"Switching to proxy {new_proxy}")
            L.context._session.proxies = {"https": new_proxy, "http": new_proxy}
        else:
            # If the list of proxies is empty, raise an exception and exit the loop
            raise Exception("All proxies failed") from None
