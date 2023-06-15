import time
from pypresence import Presence
from time import sleep
from config import APP_ID
import json
import os

def debug(*args, **kwargs):
    print("[DEBUG]", end=" ")
    print(*args, **kwargs)

def error(*args, **kwargs):
    print("[ERROR]", end=" ")
    print(*args, **kwargs)

def info(*args, **kwargs):
    print("[INFO]", end=" ")
    print(*args, **kwargs)

info("Starting Discord Presence...")

debug(os.environ.get("XDG_RUNTIME_DIR"))
# make /tmp/lurifosterm directory if not exists
if not os.path.exists("/tmp/lurifosterm"):
    os.makedirs("/tmp/lurifosterm")
    info("Created /tmp/lurifosterm directory")
else:
    info("/tmp/lurifosterm directory already exists")


info("Connecting to Discord...")
# main loop
RPC = Presence(APP_ID)

while 1:
    try:
        RPC.connect()
        info("Connected to Discord")
        break
    except Exception as e:
        error(e)
        sleep(15)
        continue
lasttimeerror = False

while 1:
    try:
        if lasttimeerror:
            info("Reconnecting to Discord...")
            RPC.connect()
            info("Connected to Discord")

        # check if file /tmp/lurifosterm/config.json exists
        if os.path.isfile("/tmp/lurifosterm/config.json"):
            data = json.load(open("/tmp/lurifosterm/config.json"))
            details = data.get("details")
            state = data.get("state")
            large_image = data.get("large_image")
            large_text = data.get("large_text")
            small_image = data.get("small_image")
            small_text = data.get("small_text")
        else:
            # details = "Playing Valorant"
            # state = "In a match"
            # large_text = "Lurifos's Terminal"
            # small_image = "valorant"
            # small_text = "Killjoy#SIMP"
            details = "Trying sudo userdel -r lurifos"
            state = "depressed"
            large_image = "default"
            large_text = "Lurifos's Terminal"
            small_image = "depressed"
            small_text = "depressed"
            
        
        buttons = [
             {"label": "whoami", "url": "https://lurifos.dev"}]

        # update pypresence
        RPC.update(
                details=details,
                state=state,
                large_image= large_image,
                large_text=large_text,
                small_image=small_image,
                small_text=small_text,
                buttons=buttons,
                start= int(time.time())
                )
        info("Updated Discord Presence")
        lasttimeerror = False
        
    except Exception as e:
        error(e)
        lasttimeerror = True

    finally:
        # sleep 15 seconds
        sleep(15)


