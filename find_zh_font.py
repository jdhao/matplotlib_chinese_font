import matplotlib.font_manager as mfm
import subprocess
import simplejson as json
import shlex


def save_zh_font():
    command = "fc-list :lang=zh -f '%{file},%{family[0]}\n'"
    args = shlex.split(command)
    output = subprocess.check_output(args)
    result = output.decode('utf-8').split('\n')

    fpths = []
    fnames = []
    for item in result:
        try:
            file, name = item.split(',')
            if file not in fpths:
                fpths.append(file)
                fnames.append(name)
        except ValueError:
            pass

    with open("zh_font_pth_name.json", "w") as f:
        json.dump(list(zip(fpths, fnames)), f)

    zh_font_name = set(fnames)
    mpl_font = set([f.name for f in mfm.fontManager.ttflist])

    valid_zh_font = list(mpl_font.intersection(zh_font_name))

    with open("valid_zh_font.json", "w") as f:
        json.dump(valid_zh_font, f)
