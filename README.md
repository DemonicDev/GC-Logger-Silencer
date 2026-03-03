### GC-Logger-Silencer
You are free to use this Script
Tested on 5.41.0 Vanilla Pmmp
no guarantee it will work for ever, when PMMP decides to change the GarbageCollectorManager.php, this will most likely break
Usage on own Risk!

I made this script, since i was annoyed by the Garbage Collection Logs in Console, so it Comments out the Logger->info part in the GarbageCollectorManager Class

# Debug on:
![image](https://github.com/user-attachments/assets/e0da7cfb-8145-435c-8264-0abd33a3efa2)

# Debug off:
![image](https://github.com/user-attachments/assets/4c9a628f-fac5-48da-958d-7cec06cfdf69)

also advantage of this Script is, that the GC-Logs arent saved in server.log

Now The big Question: how to apply this if this isnt a plugin?
# Manual Usage
## 1
Head to [Pocketmine-Mp](https://github.com/pmmp/PocketMine-MP) Github Repo, and download the Source-Code, or a fork of pmmp (not tested, but might work on [Nethergames](https://github.com/NetherGamesMC/PocketMine-MP) multiversion pmmp)
put it in the folder where u want to build Pocketmine-MP.phar
## 2 
Download GCR.py (short for GarbageCollectorspamRemover) and put it also in the folder
<img width="686" height="135" alt="image" src="https://github.com/user-attachments/assets/48421a07-a51f-4934-bde4-c7aac81ead13" />
(on my local pc i used the old File name my bad)
## 3 
open cmd and run "py GCR.py
<img width="968" height="326" alt="image" src="https://github.com/user-attachments/assets/05bfe377-d7a3-4953-9276-d80a51792aaf" />
Result:
<img width="989" height="260" alt="image" src="https://github.com/user-attachments/assets/2bf96bd5-d282-4e12-938c-5bec094a7af1" />
## 4 
download The [Pocketmine-Builder](https://github.com/DemonicDev/PocketMine-Builder/blob/main/Lite.py)
and put the bin folder u use for ur Pocketmine Server (depending on OS!) in the path
<img width="660" height="156" alt="image" src="https://github.com/user-attachments/assets/0d074382-00a3-4091-ad6c-a7a31c426d58" />
## 5
run it with "py Lite.py"
<img width="1255" height="542" alt="image" src="https://github.com/user-attachments/assets/74ab7e39-e7bf-422c-8eb6-7bd57dc468f6" />
open then the output folder, where u will find ur Build Pocketmine-MP.phar with disabled GC Spam.
The downside of this approach is, that u will need to repeat this process each Pocketmine Update, but this is the only working solution i found after some brainstorming without nuking the asyncworkers


