#coding:utf8
#!/usr/bin/python
from PIL import Image,ImageDraw,ImageFont

def add(img):
    draw = ImageDraw.Draw(img)
    #Arial.ttf是电脑上安装的字体，size是字体大小
    myfont = ImageFont.truetype('C:\Windows\Fonts\Arial.ttf',size=30)
    #填充的颜色
    fillcolor = "#FF0000"
    print(img.size)
    #向图片对象添加位置40,40 内容为1 字体font 填充颜色设置
    draw.text((350,5),'999+',font=myfont,fill=fillcolor)
    #保存图片
    img.save(r"C:\Python27\2.jpg",'jpeg')
#open picture
img = Image.open(r"C:\Python27\1.jpg")
add(img)
img.show()
