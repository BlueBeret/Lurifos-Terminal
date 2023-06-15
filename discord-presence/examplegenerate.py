import json
from time import sleep, time

while 1:
    data = {
            "details" : "Editing framework.py",
            "state" : "Workspace: learning",
            "large_image" : "python",
            "large_text": "Python",
            "small_image": "default",
            "small_text": "Catttty",
            "last_updated" : int(time())
            }
    
    with open("/tmp/lurifosterm/config.json", "w") as outfile:
        outfile.write(json.dumps(data))
    sleep(15)
    
