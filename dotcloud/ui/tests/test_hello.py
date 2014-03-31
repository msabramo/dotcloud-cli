import os

import pytest

from dotcloud.ui import CLI


def test_hello():
    url = os.environ.get('DOTCLOUD_API_ENDPOINT', 'https://ws.dotcloud.com/1.0')
    cli = CLI(endpoint=url)
    with pytest.raises(SystemExit):
        cli.run(['--version'])
