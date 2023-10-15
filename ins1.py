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

try:
    # Initialize the Instagram Private API
    api = Client(user_name, password)
    print("\033[32m [•] login successful ")

    while True:
        # Random search query for verified accounts
        search_query = "verified"
        results = api.search_users(search_query)

        if 'users' in results and len(results['users']) > 0:
            random_user = choice(results['users'])
            random_username = random_user['username']
            print(f"\n \033[1;33m Following {random_username} ....\033[0m")
            time.sleep(3)
            try:
                user_id = random_user['pk']
                api.friendships_create(user_id)

                # Get the user's recent posts
                user_feed = api.user_feed(user_id)
                if 'items' in user_feed:
                    for post in user_feed['items']:
                        media_id = post['id']
                        api.post_like(media_id)
                        print(f"Like action successful for post {media_id}")
                        time.sleep(45)
                        api.friendships_destroy(user_id)
                        print(f"Unfollow action successful for {random_username}")

            except Exception as e:
                print(f"Error while interacting with {random_username}: {e}")

            print("Wait for 45 seconds, don't exit")
            time.sleep(45)

            # Reinitialize the API for unfollowing
            api = Client(user_name, password)
            try:
                api.friendships_destroy(user_id)
                print(f"Unfollow action successful for {random_username}")
                time.sleep(3)
            except Exception as e:
                print(f"Error while unfollowing {random_username}: {e}")

        time.sleep(70)

except Exception as e:
    print(f"An error occurred: {e}")
