'''
Created on 16 Oct 2014

@author: mayank
'''
from PIL import Image, ImageChops

point_table = ([0] + ([255] * 255))

def _imgdiff(a, b):
    diff = ImageChops.difference(a, b)
    new = None
    if diff.getbbox():
        diff = diff.convert('L')
        diff = diff.point(point_table)
        new = diff.convert('RGB')
        new.paste(b, mask=diff)
    return new

def img_cmp(a, b, c):
    a1 = Image.open(a)
    b1 = Image.open(b)
    if (a1.histogram() != b1.histogram()):
        c1 = _imgdiff(a1, b1)
        if c1 != None:
            c1.save(c)

#### Usage Example ####
# if __name__ == "__main__":
#     dif = img_cmp('a.png', 'a.png', 'c.png')
#     print(dif)
#     a = Image.open()
#     b = Image.open('b.png')
#     c = black_or_b(a, b)
#     c.save('c.png')