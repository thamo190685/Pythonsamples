global a

def _checkGlobal():
    print(a)

def _changeGlobal():
    print(a)
    a =+ 10

a = 10

_checkGlobal()

_changeGlobal()

_checkGlobal()
