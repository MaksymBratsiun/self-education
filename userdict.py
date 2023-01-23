from collections import UserDict


class LookUpKeyDict(UserDict):
    def lookup_key(self, value):
        return [i for i in self.data if self.data[i] == value]


look_up = LookUpKeyDict({1: 1, 2: 2, 3: 3, 4: 1})
value = 1

