# coding=utf-8

# 图像缩放
# from PIL import Image
# im = Image.open('test.png')
# w, h = im.size
# im.thumbnail((w // 2, h // 2))
# im.save('test_thumbnail.png')

# 还有其它功能，如切片、旋转、滤镜、输出文字、调色板等
# 模糊效果
# from PIL import Image, ImageFilter
#
# im = Image.open('test.png')
# im = im.filter(ImageFilter.BLUR)
# im.save('test_blur.png')

# 利用ImageDraw提供的一系列绘图方法，我们可以直接画图，比如：生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def rndChar():
    return chr(random.randint(65, 90))

def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 64 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
font = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf', 36)
draw = ImageDraw.Draw(image)
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())

for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())

image = image.filter(ImageFilter.BLUR)
image.save('verification code.jpeg')