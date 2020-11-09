import os
import argparse
import subprocess
import shutil

import glyphs_svg_to_png


def main():
    parser = argparse.ArgumentParser(description="Extract glyphs from font files.")
    parser.add_argument("-i", "--input_path", type=str, required=True, help="Directory containing all font files.")
    parser.add_argument("-o", "--output_path", type=str, required=True,
                        help="Directory where all exports will be saved")
    parser.add_argument("-svg", "--svg", action="store_true", help="Convert font to SVG files.")
    parser.add_argument("-png", "--png", action="store_true", help="Convert font to PNG files.")
    parser.add_argument("-e", "--extract_all", action="store_true",
                        help="If set this script extracts all available glyphs, else it extracts only A-Z, a-z & öäü.")
    args = parser.parse_args()

    if not os.path.isdir(args.input_path):
        raise NotADirectoryError(args.input_path)

    if not os.path.isdir(args.output_path):
        raise NotADirectoryError(args.output_path)

    if not args.svg and not args.png:
        parser.error("At least -svg or -png (or both) must be set.")

    svg_path = os.path.join(args.output_path, 'glyphs_svg')
    png_path = os.path.join(args.output_path, 'glyphs_png')

    # Extract glyphs from fonts as svg using Fontforge.
    #
    # Need to call this script by using subprocess.
    # see: https://fontforge.org/docs/scripting/python/fontforge.html
    subprocess.call(['fontforge', "-lang=py", "-script", "extract_glyphs.py",
                     args.input_path, svg_path, str(args.extract_all)])

    if args.png:
        # Convert svg files to png using Inkscape.
        glyphs_svg_to_png.convert_svg_to_png(svg_path, png_path)

    if not args.svg:
        # Remove svg files, if not wanted.
        shutil.rmtree(svg_path)


if __name__ == "__main__":
    main()
