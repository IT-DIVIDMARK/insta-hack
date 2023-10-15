import sys
import time
from random import choice
from instagram_private_api import Client

# Handle command line arguments for username and password
if len(sys.argv) < 3:
    print("Usage: python script.py <username> <password>")
    sys.exit(1)

user_name = str(sys.argv[1])
password = str(sys.argv[2])

def get_active_users(api):
    return api.get_user_tags()

try:
    # Initialize the Instagram Private API
    api = Client(user_name, password)
    print("\033[32m [•] login successful ")

    while True:
        active_users = get_active_users(api)
        if active_users:
            for _ in range(5):  # Interact with 5 active users
                random_user = choice(active_users)
                random_username = random_user['user']['username']
                user_id = random_user['user']['pk']

                print(f"\n \033[1;33m Following {random_username} ....\033[0m")
                time.sleep(3)

                try:
                    api.friendships_create(user_id)
                    print(f"Follow action successful for {random_username}")

                    # Get the user's recent posts
                    user_feed = api.username_feed(user_id)
                    if 'items' in user_feed:
                        count = 0
                        for post in user_feed['items']:
                            if count < 2:
                                media_id = post['id']
                                api.post_like(media_id)
                                print(f"Like action successful for post {media_id}")
                                count += 1

                    time.sleep(45)

                    api.friendships_destroy(user_id)
                    print(f"Unfollow action successful for {random_username}")

                except Exception as e:
                    print(f"Error while interacting with {random_username}: {e}")

            time.sleep(5)  # Check every 5 seconds for active users

except Exception as e:
    print(f"An error occurred: {e}")
