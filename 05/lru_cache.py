"""LRU Cache module"""

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
            del self._cache[key]
            self._cache[key] = value
        return value

    def set(self, key, value):
        """set method"""
        if self.size + 1 > self.limit:
            del self._cache[list(self._cache.keys())[0]]
        self._cache[key] = value
        self.size += 1


# if __name__ == "__main__":
#     pass
    # cache = LRUCache(2)

    # cache.set("k1", "val1")
    # cache.set("k2", "val2")

    # assert cache.get("k3") == None
    # assert cache.get("k2") == "val2"
    # assert cache.get("k1") == "val1"

    # cache.set("k3", "val3")
    # print(cache._cache)
    # assert cache.get("k3") == "val3"
    # assert cache.get("k2") == None
    # assert cache.get("k1") == "val1"
