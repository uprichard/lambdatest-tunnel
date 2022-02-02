# lambdatest-tunnel-manager

[![Python application](https://github.com/uprichard/lambdatest-tunnel-manager/actions/workflows/python-app.yml/badge.svg)](https://github.com/uprichard/lambdatest-tunnel-manager/actions/workflows/python-app.yml)

Python bindings for LambdaTest Tunnel.

### Installation

```sh
pip install lambdatest-tunnel-manager
```

### Example

```python
from lambdatest_tunnel.tunnel import LambdaTunnel

# creates an instance of Tunnel manager
# replace <user> & <key> with your key. You can also set an environment variable - "LT_USERNAME" & "LT_ACCESS_KEY" instead of passing in user and key
lt_tunnel = LambdaTunnel({ "--user": "<user>", "--key": "<key>" })

# starts the tunnel instance
lt_tunnel.start()

# stop the tunnel instance
lt_tunnel.stop()
```

### Arguments

You can pass any of the LambdaTest cmdline arguments to the tunnel manager.
For the full list, refer [Tunnel options](https://www.lambdatest.com/support/docs/lambda-tunnel-modifiers/). For examples:

#### Multiple Tunnels
If doing simultaneous multiple connections, set this uniquely for different processes - 
```sh
tunnel_args = { "--infoAPIPort": "random_port", "--tunnelName": "random_string"}
```


### Contribute

To run the test suite run, `python -m unittest discover`.

Note: "LT_USERNAME" & "LT_ACCESS_KEY" befoer running the tests

### Reporting bugs

You can submit bug reports to the the Github issue tracker.

Before submitting an issue please check if there is already an existing issue. If there is, please add any additional information give it a "+1" in the comments.

When submitting an issue please describe the issue clearly, including how to reproduce the bug, which situations it appears in, what you expect to happen, what actually happens, and what platform (operating system and version) you are using.

### Pull Requests

Please keep the following in mind.

* Follow coding conventions you see in the surrounding code.
* Include tests, and make sure all tests pass.
