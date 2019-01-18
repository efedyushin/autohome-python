import sys
import argparse

import pathlib
import trafaret
from trafaret_config import ConfigError, commandline
from aiohttp import web

PATH = pathlib.Path(__file__).parent.parent
DEFAULT_CONFIG_PATH = PATH / 'config' / 'config.yaml'
TRAFARET = trafaret.Dict({'SECRET': trafaret.String(),
                          'IP': trafaret.String(),
                          'HOST': trafaret.String(),
                          'PORT': trafaret.Int()
                          })


def get_config(argv=None) -> dict:
    try:
        ap = argparse.ArgumentParser()
        commandline.standard_argparse_options(
            ap,
            default_config=DEFAULT_CONFIG_PATH,
        )
        options = ap.parse_args(argv)
        config = commandline.config_from_options(options, TRAFARET)
        return config
    except ConfigError as e:
        e.output()
        sys.exit(1)


def init_config(app: web.Application, argv=None) -> None:
    app['config'] = get_config(argv or ['-c', DEFAULT_CONFIG_PATH.as_posix()])
