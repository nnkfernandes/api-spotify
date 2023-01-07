import requests

CLIENT_ID = '5c9753b10d934d0aa213d2cc3e464918'
CLIENT_SECRET = '29b37d0d85d14a62bcaaa5dd51c03a83'

AUTH_URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

headers = {
        'Authorization': 'Bearer {token}'.format(token=access_token)
        
}

# base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

track_id = '01z2fBGB8Hl3Jd3zXe4IXR'

# actual GET request with proper header
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()

f = open("auth_response_data.txt", "w")

# Write the string to the file
resp = r

resp = resp.text

f.write(resp)

# Close the file
f.close()
