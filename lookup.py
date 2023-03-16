import os
import glob
import requests
from coloramma import init, Fore xDDD

init()

# set the path to your playerdata folder
playerdata_path = 'ENTER/YOUR/PATH/HERE'

# set the output file name
output_file = 'uuids.txt'

# check if the playerdata folder exists
if not os.path.exists(playerdata_path):
    print(f'Error: Playerdata folder not found at {playerdata_path}')
    exit()

# get a list of all player data files
player_files = glob.glob(f'{playerdata_path}/*.dat')

# check if any player data files were found
if not player_files:
    print(f'Error: No player data files found in {playerdata_path}')
    exit()

# open the output file for writing
with open(output_file, 'w') as f:
    # loop through each player data file
    for player_file in player_files:
        # extract the UUID from the file name
        uuid = os.path.splitext(os.path.basename(player_file))[0]
        # build the URL for the player's name history
        url = f'https://api.mojang.com/user/profile/{uuid}'
        # send a GET request to the URL
        response = requests.get(url)
        # check if the request was successful
        if response.status_code != 200:
            print(f'Error: Failed to get data for UUID {uuid}')
            continue
        # parse the JSON content of the response
        data = response.json()
        # get the player's current username
        username = data['name']
        # write the UUID and username to the output file
        f.write(f'{username.ljust(20)} - {uuid} \n')

print(Fore.GREEN + 'Done!')
