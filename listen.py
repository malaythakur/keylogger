from pynput.mouse import Listener


def writetofile(x, y):
    print('Position of current mouse {}'.format((x, y)))


with Listener(on_move=writetofile) as l:
    l.join()
