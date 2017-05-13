import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import simplejson as json
from find_zh_font import save_zh_font
import os
import argparse

if os.path.isfile('valid_zh_font.json') and os.path.isfile('zh_font_pth_name.json'):
    pass
else:
    save_zh_font()

parser = argparse.ArgumentParser(description="Choose which method you want to use")
parser.add_argument("--method",type=str, default="method1",choices=['method1', 'method2', 'method3'],
                    help="method you want to use",)
args = parser.parse_args()

fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xticks([])
ax.set_yticks([])
ax.set_facecolor('#181A1C')
mpl.rcParams['axes.unicode_minus'] = False
alignment = {'horizontalalignment': 'left', 'verticalalignment': 'baseline'}
default_size = fig.get_size_inches()


if args.method == 'method1':

    with open('zh_font_pth_name.json', 'r') as f:
        font_info = json.load(f)
    size = len(font_info)
    step = 1.0/size
    fig.set_size_inches(default_size[0]*1, default_size[1]*2)

    print("{} fonts available".format(size))
    for i, (path, name) in enumerate(font_info):

        font = fm.FontProperties(fname=path)
        ax.text(x=0.3,y=0.985-i*step, s=u'龙飞凤舞 ' + '(' + name + ')',
                color='#FFFFFF', fontproperties=font, **alignment)
    #plt.savefig('test.png',dpi='figure')

if args.method == 'method2':
    with open("valid_zh_font.json", "r") as f:
        valid_zh_font = json.load(f)

    size = len(valid_zh_font)
    step = 1.0/size
    fig.set_size_inches(default_size[0], default_size[1]*2)
    print("{} fonts available".format(size))

    for i, name in enumerate(valid_zh_font):
        ax.text(x= 0.3,y=0.97-i*step, s=u'龙飞凤舞 '+"(" + name+")",
                    color='#FFFFFF', fontname=name, **alignment)

if args.method == 'method3':

    with open("valid_zh_font.json", "r") as f:
        valid_zh_font = json.load(f)

    if len(valid_zh_font) == 0:
        raise ValueError("No available zh font to use.\n"
                         "valid_zh_font num is {}".format(len(valid_zh_font)))

    size = len(valid_zh_font)
    step = 1.0 / size
    fig.set_size_inches(default_size[0], default_size[1] * 2)
    print("{} fonts available".format(size))

    for i, name in enumerate(valid_zh_font):
        mpl.rcParams['font.family']= name
        # mpl.rcParams['font.family']= 'sans-serif'
        # mpl.rcParams['font.sans-serif'] = name

        ax.text(x=0.3, y=0.97 - i * step, s=u'龙飞凤舞 ' + "(" + name + ")",
                color='#FFFFFF', **alignment)

plt.show()
