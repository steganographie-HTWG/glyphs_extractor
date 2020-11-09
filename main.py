import os
import argparse
import subprocess

import glyphs_svg_to_png


def main():
    parser = argparse.ArgumentParser(description="Extract glyphs from font-files.")
    parser.add_argument("-i", "--input_path", type=str, required=True)
    parser.add_argument("-o", "--output_path", type=str, required=True)
    parser.add_argument("-r", "--remove_svg", action="store_true",
                        help="If True, removes all svg files.")
    parser.add_argument("-e", "--extract_all", action="store_true",
                        help="If False, this script extracts only A-Z, a-z & öäü, else it extracts all glpyhs.")
    args = parser.parse_args()

    if not os.path.isdir(args.input_path):
        raise NotADirectoryError(args.input_path)

    if not os.path.isdir(args.output_path):
        raise NotADirectoryError(args.output_path)

    if args.remove_svg:
        raise NotImplemented("This function is not yet implemented.")

    if args.extract_all:
        raise NotImplemented("This function is not yet implemented.")

    subprocess.call(['fontforge', "-lang=py", "-script", "extract_glyphs.py", args.input_path, args.output_path],
                    stdout=open(os.devnull, 'wb'))

    glyphs_svg_to_png.convert_svg_to_png(
        svg_glyph_path=os.path.join(args.output_path, 'glyphs_svg'),
        output_path=args.output_path
    )


if __name__ == "__main__":
    main()
