from __future__ import print_function, division
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib as mpl
import simplejson as json
from find_zh_font import save_zh_font
from os.path import isfile
import argparse
import math


def get_layout(font_num=None):

    num = int(math.ceil(font_num/2.0))

    return num, 1.0/num


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Choose which method you "
                                                 "want to use")
    parser.add_argument("--method",
                        type=str,
                        default="m1",
                        choices=['m1', 'm2', 'm3'],
                        help="method you want to use")

    args = parser.parse_args()

    if isfile('valid_zh_font.json') and isfile('zh_font_pth_name.json'):
        pass
    else:
        save_zh_font()

    fig, ax = plt.subplots(figsize=(8,10))

    ax.set_facecolor('#181A1C')
    mpl.rcParams['axes.unicode_minus'] = False

    alignment = {'horizontalalignment': 'left',
                 'verticalalignment': 'baseline'}
    """
    default_size = fig.get_size_inches()
    fig.set_size_inches(default_size[0] * 1.5, default_size[1] * 2)
    """
    if args.method == 'm1':

        with open('zh_font_pth_name.json', 'r') as f:
            font_info = json.load(f)

        num_font_per_col, step = get_layout(len(font_info))

        for i, (path, name) in enumerate(font_info):

            font = fm.FontProperties(fname=path)

            if i < num_font_per_col:
                ax.text(x=0.1,y=0.97-i*step,
                        s=u'龙飞凤舞 ( %s )' % name,
                        color='#FFFFFF',
                        fontproperties=font,
                        **alignment)
            else:
                j = i - num_font_per_col
                ax.text(x=0.6, y=0.97-j*step,
                        s=u'龙飞凤舞 ( %s )' % name,
                        color='#FFFFFF',
                        fontproperties=font,
                        **alignment)

    if args.method in ['m2', 'm3']:

        with open("valid_zh_font.json", "r") as f:
            valid_zh_font = json.load(f)

        if len(valid_zh_font) == 0:
            raise ValueError("No available zh font to use.\n")

        num_font_per_col, step = get_layout(len(valid_zh_font))

        if args.method == 'm2':

            for i, name in enumerate(valid_zh_font):

                if i < num_font_per_col:
                    ax.text(x= 0.1,y=0.95-i*step,
                            s=u'龙飞凤舞 ( %s )' % name,
                            color='#FFFFFF',
                            fontname=name,
                            **alignment)
                else:
                    j = i - num_font_per_col
                    ax.text(x=0.5, y=0.95-j*step,
                            s=u'龙飞凤舞 ( %s )' % name,
                            color='#FFFFFF',
                            fontname=name,
                            **alignment)

        if args.method == 'm3':

            for i, name in enumerate(valid_zh_font):
                mpl.rcParams['font.family']= name
                # mpl.rcParams['font.family']= 'sans-serif'
                # mpl.rcParams['font.sans-serif'] = name
                if i < num_font_per_col:
                    ax.text(x=0.1, y=0.95 - i * step,
                            s=u'龙飞凤舞 ( %s )' % name,
                            color='#FFFFFF',
                            **alignment)
                else:
                    j = i-num_font_per_col
                    ax.text(x=0.5, y=0.95 - j* step,
                            s=u'龙飞凤舞 ( %s )' % name,
                            color='#FFFFFF',
                            **alignment)

    ax.set_xticks([])
    ax.set_yticks([])

    # adjust the axes aspect ratio
    xleft, xright = ax.get_xlim()
    ybottom, ytop = ax.get_ylim()
    # the abs method is used to make sure that all numbers are positive
    # because x and y axis of an axes maybe inversed.
    ax.set_aspect(abs((xright - xleft) / (ybottom - ytop)) * 1.5)
    fig.tight_layout()

    plt.savefig('sample_output.jpg', bbox_inches='tight')
    plt.show()

