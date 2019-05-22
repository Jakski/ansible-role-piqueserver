import os
import json

import testinfra.utils.ansible_runner


testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_service(host):
    piqueserver = host.service('piqueserver')
    assert piqueserver.is_running
    assert piqueserver.is_enabled
    assert host.socket('udp://127.0.0.1:32887').is_listening


def test_configuration(host):
    config = host.file('/etc/piqueserver/config.json')
    parsed_config = json.loads(config.content_string)
    assert parsed_config['logfile'] == '/var/log/piqueserver/log.txt'
    assert parsed_config['bans']['file'] == '/var/lib/piqueserver/bans.txt'


def test_persistent_data(host):
    assert host.file('/var/lib/piqueserver/maps/classicgen.txt').exists
    assert host.file('/var/log/piqueserver/log.txt').exists
