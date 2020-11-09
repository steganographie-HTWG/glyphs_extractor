import os
from os import path
import pathlib
import subprocess

import progressbar


SVG_GLYPH_PATH = 'glyphs_svg'

SVG_GLYPH_COUNT = len([os.path.join(dp, f) for dp, dn, filenames in os.walk(SVG_GLYPH_PATH) for f in filenames if os.path.splitext(f)[1] == '.svg'])

bar = progressbar.ProgressBar(max_value=SVG_GLYPH_COUNT)
i = 0


for (dirpath, dirnames, filenames) in os.walk(SVG_GLYPH_PATH):
    if dirpath != SVG_GLYPH_PATH:
        png_dir = path.join('glyphs_png', path.split(dirpath)[1])
        pathlib.Path(png_dir).mkdir(parents=True, exist_ok=True)

        for filename in filenames:
            svg_filepath = path.join(os.getcwd(), dirpath, filename)
            png_filepath = path.join(png_dir, path.splitext(filename)[0] + '.png')

            subprocess.call(['inkscape', svg_filepath, '-z', '-D', '-e', png_filepath, '-b', 'white'], stdout=open(os.devnull, 'wb'))

            i += 1
            bar.update(i)
