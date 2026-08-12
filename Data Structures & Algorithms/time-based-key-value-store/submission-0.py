class TimeMap:

    def __init__(self):
        self.key_store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        value_time_arr = self.key_store.get(key, [])

        l, r = 0, len(value_time_arr) - 1

        while l <= r:
            m = (l + r) // 2
            
            if value_time_arr[m][1] <= timestamp:
                res = value_time_arr[m][0]
                l = m + 1
            else:
                r = m - 1
        
        return res
