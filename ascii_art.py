"""
Usage:
    ascii [options] <inputfile> [<outputfile>]

Options:
    -h --help         how to use?
    -o                 asd
    --output=FILE      output [default: ascii.txt]
    --width=W          image width [default: 80]
    --height=H         image height [default: 80]

"""

from PIL import Image
from docopt import docopt

arguments = docopt(__doc__)
Img = arguments['<inputfile>']
Width = int(arguments['--width'])
Height = int(arguments['--height'])
Output = arguments['<outputfile>'] if arguments['<outputfile>'] != None else arguments['--output']

# 字符集，用于填充字符画
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

# 根据红、绿、蓝三个分量的值来获取相应灰度值并根据灰度值返回字符
def get_char(r, g, b, alpha = 256):
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int(0.299 * r + 0.587 * g + 0.114 * b)

    unit = (256.0 + 1)/length
    return ascii_char[int(gray/unit)]

if __name__ == '__main__':

    im = Image.open(Img)
    # 将图片转换为像素为Width X Height的图片
    im = im.resize((Width,Height), Image.NEAREST)

    txt = ""
    # 以每个像素的为单位填充相应灰度值的字符串字符串
    for i in range(Height):
        for j in range(Width):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'

    #字符画输出到文件
    with open(Output,'w') as f:
            f.write(txt)
