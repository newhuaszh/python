# coding=utf-8
from PIL import Image

try:
    with Image.open(u'积分事件.PNG') as im:
        box = (10, 10, 40, 40)
        x, y = 6, 16
        w, h = 28, 25
        num = 0
        while y + h <= 90:
            x = 5
            while x + w <= 385:
                box = (x, y, x + w - 2, y + h)
                region = im.crop(box)
                num += 1
                region.save(ur'.\splited_img\%s.PNG' % num)
                region.close()
                x += w + 1

            y += h + 1


except StandardError, e:
    print e
finally:
    print 'done'