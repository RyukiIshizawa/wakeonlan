from crontab import CronTab
from pathlib import Path
import getpass

proj_path = Path(__file__).parent
cmd = '{} {}'.format(proj_path / '.venv/bin/python', proj_path / 'main.py')

# 実行ユーザーのcronを取得
cron = CronTab(user=getpass.getuser())
job = cron.new(command=cmd)

# 再起動後、main.pyを実行
job.every_reboot()

cron.write_to_user(user=True)

for job in cron:
    print(job)