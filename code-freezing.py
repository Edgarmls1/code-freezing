import logging
import sys

import yaml

CONFIG_FILE = "config.yml"

logging.basicConfig(
    format="[%(asctime)s] [%(levelname)s] - %(message)s",
    datefmt="%m-%d-%Y %I:%M:%S",
    level=logging.DEBUG
)

def get_config(file_name: str) -> dict:
    with open(file_name) as f:
        return yaml.safe_load(f)


def unpack_config(config: dict) -> tuple:
    try:
        bypass_group = config["bypass_group"]
        freezing_dates = config["freezing_dates"]
    except KeyError:
        logging.error(f"one of the fields are not present: 'bypass_group' or 'freezing_dates' on file '{CONFIG_FILE}'")
        sys.exit(1)
    
    return (bypass_group, freezing_dates)


def main():
    config = get_config(CONFIG_FILE)
    bypass_group, freezing_dates = unpack_config(config)

    logging.info(bypass_group)
    logging.info(freezing_dates)

if __name__ == "__main__":
    main()
