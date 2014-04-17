import pickle
import subprocess
import StringIO

class BadTest(object):
    def __init__(self):
        pass

    def __reduce__(self):
        return (subprocess.Popen, (["ls", "-l"],))


class GoodTest(object):
    def __init__(self):
        pass

class GoodTestOld():
    def __init__(self):
        pass

class   SecureUnpickler(pickle.Unpickler):
    def load(self):
        for line in self.read().split("\n"):
            print(line)

    @classmethod
    def loads(cls, s):
        return cls(StringIO.StringIO(s)).load()


bad_obj = pickle.dumps(BadTest())
good_obj = pickle.dumps(GoodTest())
good_obj_old = pickle.dumps(GoodTestOld())

SecureUnpickler.loads(bad_obj)
print("")
SecureUnpickler.loads(good_obj)
print("")
SecureUnpickler.loads(good_obj_old)

import copy_reg

print(copy_reg._reconstructor)
