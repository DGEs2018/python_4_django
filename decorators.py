def announce(f):
    def wrapper():
        print('...about to run function')
        f()
        print('Done with the function')
    return wrapper
@announce
def howdy():
    print('Hey all !')

howdy()