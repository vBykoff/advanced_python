"""LRU Cache module"""
import logging
import sys


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class LRUCache:
    """Lru cache"""

    def __init__(self, limit=42):
        self.size = 0
        self.limit = limit
        self._cache = {}

    def get(self, key):
        """get method"""
        value = self._cache.get(key)
        if value is not None:
            logger.info("Getting from existing key")
            del self._cache[key]
            self._cache[key] = value
        else:
            logger.info("Getting from not existing key")
        return value

    def set(self, key, value):
        """set method"""
        if self.size + 1 > self.limit:
            logger.info("Size reached limit")
            logger.info(
                    f"Deleting ({list(self._cache.keys())[0]},"
                    f"{self._cache[list(self._cache.keys())[0]]})"
            )
            del self._cache[list(self._cache.keys())[0]]
        if key in self._cache.keys():
            logger.info("Setting an existing key")
        else:
            logger.info("Setting not existing key")

        logger.info(f"Setting ({key}, {value})")
        self._cache[key] = value
        self.size += 1


def checking_argumetns():
    """Defining logger"""
    if "-s" in sys.argv:
        stdout_handler = logging.StreamHandler(sys.stdout)
        stdout_handler.setLevel(logging.DEBUG)
        stdout_formatter = logging.Formatter("%(asctime)s\t%(name)s\t"
                                             "%(levelname)s\t%(message)s")
        stdout_handler.setFormatter(stdout_formatter)
        logger.addHandler(stdout_handler)

    file_formatter = logging.Formatter("%(asctime)s\t%(name)s\t"
                                       "%(levelname)s\t%(message)s")
    file_handler = logging.FileHandler("cache.log")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)


def run():
    """Testing Lru cache"""
    cache = LRUCache(2)

    cache.set("k1", "val1")
    cache.set("k2", "val2")

    assert cache.get("k3") is None
    assert cache.get("k2") == "val2"
    assert cache.get("k1") == "val1"

    cache.set("k3", "val3")
    assert cache.get("k3") == "val3"
    assert cache.get("k2") is None
    assert cache.get("k1") == "val1"


if __name__ == "__main__":
    checking_argumetns()
    run()
