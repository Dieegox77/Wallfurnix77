import sys

from g_python.gextension import Extension


from wallfurni import WallFurni

ext = None

extension_info = {
    "title": "WallFurni_py",
    "description": "Move wall furni",
    "version": "77.0",
    "author": "Dieegox77"
    # Original extension by kSlideHH 
    # Credits to Laande and Sirjonasxx :D
}

if __name__ == '__main__':
    extension = Extension(extension_info, sys.argv)
    extension.start()
    WallFurni(extension)
