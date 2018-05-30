class Singleton(type):
    def __init__(self, *args):
        type.__init__(self, *args)
        self._instances = {}

    def __call__(self, *args):
        if not args in self._instances:
            self._instances[args] = type.__call__(self, *args)
        return self._instances[args]

class Test:
    __metaclass__=Singleton
    def __init__(self, *args): pass

            
ta1, ta2 = Test(), Test()
assert ta1 is ta2

tb1, tb2 = Test(5), Test(5)
assert tb1 is tb2

assert ta1 is not tb1





# simpler:

def singleton(cls):
    cls._instance = cls._instance or cls()
    return cls._instance
 
 class ThreadKiller:
    _instance = None
    active = False

tk1 = singleton(ThreadKiller)
tk2 = singleton(ThreadKiller)
tk3 = singleton(ThreadKiller)

tk1.active
# False
tk2.active
# False
tk3.active
# False

tk3.active = True
tk.active
# True
tk2.active
# True
tk1.active
# True

print(tk1 is tk2 is tk3)
True

tk, tk1, tk2, tk3
#<__main__.ThreadKiller at 0x7f8578bd6fd0>,
#<__main__.ThreadKiller at 0x7f8578bd6fd0>,
#<__main__.ThreadKiller at 0x7f8578bd6fd0>,
#<__main__.ThreadKiller at 0x7f8578bd6fd0>
