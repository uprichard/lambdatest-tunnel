import unittest
import requests
from lambdatest_tunnel.tunnel import LambdaTunnel


class TestLambdaTunnel(unittest.TestCase):

    def test_start(self):
        tunnel = LambdaTunnel()
        tunnel.start()
        r = requests.get('http://127.0.0.1:8005/api/v1.0/info')
        assert r.ok
        tunnel.stop()

    def test_diff_admin_port(self):
        tunnel = LambdaTunnel({'--infoAPIPort': '8002'})
        tunnel.start()
        assert tunnel.wait_tunnel_ready()
        r = requests.get('http://127.0.0.1:8002/api/v1.0/info')
        assert r.ok
        assert tunnel.tunnel_running()
        tunnel.stop()
        assert not tunnel.tunnel_running()
