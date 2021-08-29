from graphics import *
from encodify import Encodify
import os.path

win = GraphWin("Locker", 500, 500)
win.setBackground('white')
img = Image(Point(250, 250), "back1.PNG")
img.draw(win)


def buttons():
    left = Rectangle(Point(60, 325),
                     Point(175, 360))  # points are ordered ll, ur
    right = Rectangle(Point(320, 325), Point(435, 360))

    left.draw(win)
    right.draw(win)

    return left, right,


def inside(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return (ll.getX() < point.getX() < ur.getX() \
            and ll.getY() < point.getY() < ur.getY())


def text_bx():
    try:
        bx = Entry(Point(250, 250), 10)
        bx.draw(win)
        tx = Text(Point(250, 280), "")
        tx.draw(win)

        k = ''
        while not k == 'Return':
            k = win.checkKey()
            msg = bx.getText()
        return msg

    except GraphicsError:
        pass


enc, dec = buttons()
while True:
    try:
        clickPoint = win.getMouse()

        if clickPoint is None:
            print('no mouse')
        elif inside(clickPoint, enc):
            # encrypt
            correct = True
            while correct:
                t = text_bx()
                if t is not None and os.path.isfile('./' + t):
                    correct = False
                else:
                    tt = Text(Point(250, 380), "Incorrect file name, try again")
                    tt.draw(win)
            if t is None:
                win.close()
                break
            enc = Encodify(t)
            win.close()
            win = GraphWin("Locker", 500, 500)
            win.setBackground('white')
            img = Image(Point(250, 250), "back3.PNG")
            img.draw(win)

            t = text_bx()
            if t is None:
                win.close()
                break
            enc.encrypt(t)
            win.close()
            break

        elif inside(clickPoint, dec):
            # decrypt
            correct = True
            while correct:
                t = text_bx()
                if t is not None and os.path.isfile('./' + t):
                    correct = False
                else:
                    tt = Text(Point(250, 380), "Incorrect file name, try again")
                    tt.draw(win)
            if t is None:
                win.close()
                break
            enc = Encodify(t)
            win.close()
            win = GraphWin("Locker", 500, 500)
            win.setBackground('white')
            img = Image(Point(250, 250), "back4.PNG")
            img.draw(win)

            t = text_bx()
            if t is None:
                win.close()
                break
            enc.decrypt(t)
            win.close()
            break

    except GraphicsError:
        pass

win.close()
