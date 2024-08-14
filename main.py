from wakeonlan import send_magic_packet
import json, time
from pathlib import Path

setting = json.load(open(Path(__file__).parent /'setting.json'))

for i in range(setting['max_retry']):
    time.sleep(setting['execution_delay'])

    send_magic_packet(setting['mac_addresses'])

    print(f"Sent magic packet to {setting['mac_addresses']} ({i+1}/{setting['max_retry']})")