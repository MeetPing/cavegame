from pypresence import Presence
import time

client_id = '583681179291615245'  
RPC = Presence(client_id)  
RPC.connect()


f = open("levels.txt","r")

b = f.readline()

f.close
s
Date = time.time()

RPC.update(state="Playing solo", details="Level: "+ b ,large_image="cavegame1024x1024",small_image="pickaxe1024x1024",large_text="Cave Game",small_text="Pickaxe",start=Date)  # Set the presence

while True:  
 time.sleep(1)
