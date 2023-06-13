from pypresence import Presence
from time import sleep
from config import APP_ID
import json
import os
RPC = Presence(APP_ID)

# main loop
RPC.connect()

while 1:
    try:
        # check if file /tmp/lurifosterm/config.json exists
        if os.path.isfile("/tmp/lurifosterm/config.json"):
            data = json.load(open("/tmp/lurifosterm/config.json"))
            details = data.get("details")
            state = data.get("state")
            large_text = data.get("large_text")
            small_image = data.get("small_image")
            small_text = data.get("small_text")
        else:
            details = "Playing Valorant"
            state = "In a match"
            large_text = "Lurifos's Terminal"
            small_image = "Valorant"
            small_text = "Killjoy#SIMP"
        
        buttons = [
             {"label": "whoami", "url": "https://lurifos.dev"}]

        # update pypresence
        RPC.update(
                details=details,
                state=state,
                large_image="default",
                large_text=large_text,
                small_image=small_image,
                small_text=small_text,
                buttons=buttons,
                start=1686673732
                )
        
    except Exception as e:
        print(e)
        RPC.connect()

    finally:
        # sleep 15 seconds
        sleep(15)


