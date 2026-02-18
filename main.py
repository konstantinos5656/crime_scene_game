import random
import time

friends = ["Alice", "Bob", "Charlie"]
messages = ["Watch out!", "Police nearby!", "I have info!"]

while True:
    friend = random.choice(friends)
    msg = random.choice(messages)
    print(f"{friend}: {msg}")
    time.sleep(5)
