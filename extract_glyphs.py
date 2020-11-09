import os
import sys
import pathlib

import fontforge


input_path = sys.argv[1]
output_path = sys.argv[2]
export_all = sys.argv[3].lower() == 'true'

for font_filename in os.listdir(input_path):
    font_path = os.path.join(os.getcwd(), 'fonts', font_filename)
    font = fontforge.open(font_path)

    glyph_folder = os.path.join(output_path, font_filename[:-4])
    pathlib.Path(glyph_folder).mkdir(parents=True, exist_ok=True)

    if export_all:
        selection = font.selection.all()
    else:
        selection = font.selection.select(("ranges", None), "A", "Z")
        selection.select(("more", None), ("ranges", None), "a", "z")

        for umlaut_id in [196, 214, 220, 228, 246, 252]:
            selection.select(("more", None), umlaut_id)

    for glyph_id in selection:
        try:
            glyph_filename = f"{glyph_id}_{font_filename[:-4]}_{font[glyph_id].glyphname}.svg"

            font[glyph_id].export(os.path.join(glyph_folder, glyph_filename))
        except TypeError as e:
            pass
