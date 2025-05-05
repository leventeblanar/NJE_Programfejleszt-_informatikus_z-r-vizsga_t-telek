<h2>Crontab</h2>

cron is a Unix, solaris, Linux utility that allows tasks to be automatically run in the background at regular intervals by the cron daemon.

(daemon - a program that runs as a background process)

What is cron?
- A daemon which runs at the times of system boot from /etc/int.d scripts. If needed it can be stopped/started/restart using init script or with command service crond start in Linux systems.

What is a crontab?
- is a file which contains the schedule of cron entries to be run and at specified times.
<br>

![cron](img/cron.png)


Important things to consider:
- All the files and outputs should have a relative path:
```
filepath = os.path.abspath("C:/Work/Melo/kerekes_cikktorzs/Already_pulled/kerekes_cikktorzs" + today + ".xlsx")
```
- .venv usage is different - needs a full descriptive path
```
C:\Work\Melo\torzskezeles_scripts\.venv\Scripts\python.exe
```
- include logging (print methods are not visible when running programs in cron)
```
logfile = open("/home/levi/logs/cikktorzs_cron.log", "a", encoding="utf-8")
sys.stdout = logfile
sys.stderr = logfile
```
- do not use unput() or GUI things
- config file path (db_config.py) - script needs to be run in the same folder as the db_config.py file 
```
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from db_config import s
```