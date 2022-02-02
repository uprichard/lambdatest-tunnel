import unittest
import shutil
import os
from lambdatest_tunnel.tunnel_binary import LambdaTunnelBinary


class TestLambdaTunnelBinary(unittest.TestCase):

    def setUp(self):
        self.binary_dir = os.path.join(os.path.expanduser('~'), '.lambdatest')
        self.local_binary = os.path.join(self.binary_dir, 'LT')
        self.tunnel = LambdaTunnelBinary()

    def tearDown(self):
        pass

    def test_download_directory(self):
        # Delete directory
        shutil.rmtree(self.binary_dir, ignore_errors=True)
        assert self.tunnel.get_download_directory() == self.binary_dir
        # Check directory exists
        assert os.path.isdir(self.binary_dir)

    def test_binary_path(self):
        exp = os.path.join(self.binary_dir, 'LT')
        assert self.tunnel.local_binary == exp

    def test_remote_binary_path(self):
        assert self.tunnel.remote_binary_path().startswith('https://downloads.lambdatest.com/tunnel/')

    def test_download(self):
        if os.path.exists(self.local_binary): os.remove(self.local_binary)
        assert self.tunnel.download() == self.local_binary
        assert os.path.isfile(self.local_binary)
