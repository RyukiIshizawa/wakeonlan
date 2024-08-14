from crontab import CronTab
from pathlib import Path
import re, getpass

proj_path = Path(__file__).parent
cmd = re.compile('{} {}'.format(proj_path / '.venv/bin/python', proj_path / 'main.py'))

cron = CronTab(user=getpass.getuser())
job = cron.find_command(cmd)
cron.remove(job)
cron.write_to_user(user=True)

if len(cron) > 0:
    for job in cron:
        print(job)
else:
    print('No Job is written.')