from wakeonlan import send_magic_packet
import json, time
from pathlib import Path

setting = json.load(open(Path(__file__).parent /'setting.json'))

time.sleep(setting['execution_delay'])

send_magic_packet(setting['mac_addresses'])