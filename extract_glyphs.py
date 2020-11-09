import os
import pathlib
import fontforge

UMLAUTE = {
    'adieresis': 'ä',
    'odieresis': 'ö',
    'udieresis': 'ü'
}


def export_glyphs(_glyphID, tag):
    glyphname = font[_glyphID].glyphname

    if glyphname.lower() in UMLAUTE.keys():
        glyphname = UMLAUTE[glyphname.lower()]

    glyph_filename = font_filename[:-4] + tag + glyphname.lower() + '.svg'

    font[glyphID].export(os.path.join(glyph_folder, glyph_filename))
    print(glyphID, glyphname)


for font_filename in os.listdir('fonts'):
    font_path = os.path.join(os.getcwd(), 'fonts', font_filename)
    font = fontforge.open(font_path)

    glyph_folder = os.path.join(os.getcwd(), 'glyphs_svg', font_filename[:-4])
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