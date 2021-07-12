import os
import json
import logging
import logging.config

default_path='./logging.json'
default_level=logging.INFO
env_key='LOG_CFG'

class Logger:

    def getLogger(name):
        path = default_path
        value = os.getenv(env_key, None)
        if value:
            path = value
        if os.path.exists(path):
            with open(path, 'rt') as f:
                config = json.load(f)
            logging.config.dictConfig(config)
        else:
            logging.basicConfig(level=default_level)

        return logging.getLogger(name)