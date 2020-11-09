import os
import sys
import pathlib

import fontforge


def export_glyphs(_glyphID, tag):
    glyphname = font[_glyphID].glyphname

    glyph_filename = font_filename[:-4] + tag + glyphname.lower() + '.svg'

    font[glyphID].export(os.path.join(glyph_folder, glyph_filename))
    print(glyphID, glyphname)


input_path = sys.argv[1]
output_path = sys.argv[2]

for font_filename in os.listdir(input_path):
    font_path = os.path.join(os.getcwd(), 'fonts', font_filename)
    font = fontforge.open(font_path)

    glyph_folder = os.path.join(output_path, font_filename[:-4])
    pathlib.Path(glyph_folder).mkdir(parents=True, exist_ok=True)

    # uppercase a-z
    for glyphID in font.selection.select(("ranges", None), "A", "Z"):
        export_glyphs(glyphID, '_upper_')

    # uppercase Umlaute
    for glyphID in [196, 214, 220]:
        export_glyphs(glyphID, '_upper_')

    # lowercase a-z
    for glyphID in font.selection.select(("ranges", None), "a", "z"):
        export_glyphs(glyphID, '_lower_')

    # lowercase Umlaute
    for glyphID in [228, 246, 252]:
        export_glyphs(glyphID, '_lower_')