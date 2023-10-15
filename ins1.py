import sys
import time
from instagram_private_api import Client

# Handle command line arguments for username and password
if len(sys.argv) < 3:
    print("Usage: python script.py <username> <password>")
    sys.exit(1)

user_name = str(sys.argv[1])
password = str(sys.argv[2])

# List of usernames to follow and unfollow
usernames = [
    'virat.kohli', 'narendramodi', 'aliaabhatt', 'deepikapadukone', 'shraddhakapoor',
    'karanjohar', 'akshaykumar', 'priyankachopra', 'ranveersingh', 'rohitsharma45',
    'tigerjackieshroff', 'kritisanon', 'varundvn'
]

try:
    # Initialize the Instagram Private API
    api = Client(user_name, password)
    print("\033[32m [•] login successful ")

    while True:
        for username in usernames:
            print(f"\n \033[1;33m Following {username} ....\033[0m")
            time.sleep(3)
            try:
                user_info = api.username_info(username)
                user_id = user_info['user']['pk']
                api.friendships_create(user_id)

                # Get the user's recent posts
                results = api.username_feed(user_id)
                if 'items' in results:
                    for post in results['items']:
                        media_id = post['id']
                        api.post_like(media_id)
                        print(f"Like action successful for post {media_id}")
                        time.sleep(45)
                        api.friendships_destroy(user_id)
                        print(f"Unfollow action successful for {username}")

            except Exception as e:
                print(f"Error while interacting with {username}: {e}")

            print("Wait for 45 seconds, don't exit")
            time.sleep(45)

        # Reinitialize the API for unfollowing
        api = Client(user_name, password)
        for username in usernames:
            try:
                user_info = api.username_info(username)
                user_id = user_info['user']['pk']
                api.friendships_destroy(user_id)
                print(f"Unfollow action successful for {username}")
                time.sleep(3)
            except Exception as e:
                print(f"Error while unfollowing {username}: {e}")

        time.sleep(70)

except Exception as e:
    print(f"An error occurred: {e}")
