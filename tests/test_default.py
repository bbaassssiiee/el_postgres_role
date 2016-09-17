from testinfra.utils.ansible_runner import AnsibleRunner


testinfra_hosts = AnsibleRunner('.molecule/ansible_inventory').get_hosts('all')


def test_postgres_server_installed(Package):
    p = Package('postgresql94-server')
    assert p.is_installed


def test_postgres_running_and_enabled(Service):
    postgresql = Service("postgresql-9.4")
    assert postgresql.is_running
    assert postgresql.is_enabled
