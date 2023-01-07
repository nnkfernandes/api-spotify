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

f = open("filename.txt", "w")

# Write the string to the file
resp = auth_response.text

f.write(resp)

# Close the file
f.close()

