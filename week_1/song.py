import time

song ="I can hear you but I won't\nSome look for trouble\nWhile others don't\nThere's a thousand reasons\nI should go about my day\nAnd ignore your whispers\nWhich I wish would go away, oh-oh-oh\nOoh-oh-oh\nYou're not a voice\nYou're just a ringing in my ear\nAnd if I heard you, which I don't\nI'm spoken for I fear\nEveryone I've ever loved is here within these walls\nI'm sorry, secret siren, but I'm blocking out your calls\nI've had my adventure, I don't need something new\nI'm afraid of what I'm risking if I follow you\nInto the unknown\nInto the unknown\nInto the unknown"

line=song.splitlines()
for i in range(len(line)):
    print(line[i])
    time.sleep(1)
