import os
import requests
import time

def get_messages(access_token, group_id, before_id=None, max_retries=3):
    url = f'https://api.groupme.com/v3/groups/{group_id}/messages'
    params = {'token': access_token, 'limit': 100}
    if before_id:
        params['before_id'] = before_id
    
    retries = 0
    while retries < max_retries:
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception if the response contains an HTTP error status code
            return response.json()['response']['messages']
        except (requests.exceptions.RequestException, ValueError) as e:
            print(f"Error fetching messages: {e}")
            retries += 1
            time.sleep(1)  # Wait for a second before retrying

    # Return an empty list if all retries failed
    return []

# Get the access token from the environment variable
ACCESS_TOKEN = os.environ['GROUPME_ACCESS_TOKEN']

# Set up the group ID
GROUP_ID = '48214610'

# Create a folder for media if it doesn't exist
if not os.path.exists('media'):
    os.makedirs('media')

# Make the API request to get all messages in the group
all_messages = []
before_id = None

while True:
    messages = get_messages(ACCESS_TOKEN, GROUP_ID, before_id)
    if not messages:
        break
    all_messages.extend(messages)
    before_id = messages[-1]['id']

# Filter the list to only include messages with images or videos
media_messages = [m for m in all_messages if 'attachments' in m.keys() and any(a['type'] in ['image', 'video'] for a in m['attachments'])]

# Download the images and videos to the media folder
for message in media_messages:
    for attachment in message['attachments']:
        if attachment['type'] in ['image', 'video']:
            url = attachment['url']
            response = requests.get(url)
            filename = os.path.join('media', os.path.basename(url))
            with open(filename, 'wb') as f:
                f.write(response.content)

