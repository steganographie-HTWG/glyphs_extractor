import os
from os import path
import pathlib
import subprocess

import progressbar


def convert_svg_to_png(svg_glyph_path, output_path):
    SVG_GLYPH_COUNT = len([path.join(dp, f) for dp, dn, filenames in os.walk(svg_glyph_path) for f in filenames if
                           path.splitext(f)[1] == '.svg'])

    bar = progressbar.ProgressBar(max_value=SVG_GLYPH_COUNT)
    i = 0

    for (dirpath, dirnames, filenames) in os.walk(svg_glyph_path):
        if dirpath != svg_glyph_path:
            png_dir = path.join(output_path, 'glyphs_png', path.split(dirpath)[1])
            pathlib.Path(png_dir).mkdir(parents=True, exist_ok=True)

            for filename in filenames:
                svg_filepath = path.join(dirpath, filename)
                png_filepath = path.join(png_dir, path.splitext(filename)[0] + '.png')

                print(svg_filepath)
                print(png_filepath)

                subprocess.call(['inkscape', svg_filepath, '-z', '-D', '-e', png_filepath, '-b', 'white'], stdout=open(os.devnull, 'wb'))

                i += 1
                bar.update(i)
