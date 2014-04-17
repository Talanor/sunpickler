import pickle
import dis
import subprocess

class   TestClass(object):
    def __init__(self):
        pass

    
class   TestRedClass(object):
    def __init__(self):
        pass

    def __reduce__(self):
        return (subprocess.Popen, (["ls", "-l"],))

if __name__ == "__main__":
    dump1 = pickle.dumps(TestClass())

    dump2 = pickle.dumps(TestRedClass())

    print(dis.dis(dump2))

    print(dis.dis(dump1))

