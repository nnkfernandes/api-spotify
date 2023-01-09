import requests
import json

from authorization import auth

def main():

    headers = auth()

    # base URL of all Spotify API endpoints
    BASE_URL = 'https://api.spotify.com/v1/'

    #specific track id of one song
    #TODO: create a request to store 50 track_ids in an array(?).
    track_id = '4kRCp4ZtOjGn2OCtMPemiN'

    # actual GET request with proper header
    r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
    r = r.json()
    
    print(json.dumps(r, indent=2))

if __name__ == '__main__':
    main()
    
